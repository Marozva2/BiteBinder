from flask_restful import Resource, reqparse
from flask_bcrypt import Bcrypt
from models import db, User
from schema import UserSchema
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

user_schema = UserSchema()
users_schema = UserSchema(many=True)
bcrypt = Bcrypt()

class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user_schema.dump(user))

    @jwt_required()
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()


        user.username = args.get('username', user.username)
        user.email = args.get('email', user.email)
        user.password = args.get('password', user.password)

        db.session.commit()
        return jsonify(user_schema.dump(user))

    @jwt_required()
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return 'Deleted successfully', 204

class UsersResource(Resource):
    @jwt_required()
    def get(self):
        users = User.query.all()
        return jsonify(users_schema.dump(users))

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        hash_password = bcrypt.generate_password_hash(args['password']).decode('utf-8')

        new_user = User(username=args['username'], email=args['email'], password=hash_password)
        db.session.add(new_user)
        db.session.commit()
        token = create_access_token(identity=new_user.user_id)
        return jsonify({"access_token": token, "user": user_schema.dump(new_user)}), 201


class UserLoginResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        user = User.query.filter_by(username=args['username']).first()

        print(f"New username: {args['username']}, password: {args['password']}")

        if user and bcrypt.check_password_hash(user.password, args['password']):
            token = create_access_token(identity=user.user_id)
            print(f"Generated access token: {token}")
            return {"access_token": token}, 200
        else:
            print("Invalid")
            return {"msg": "Invalid"}, 401