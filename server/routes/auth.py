# authorization_resource.py
from flask_restful import Resource, reqparse
from models import db, Authorization
from schema import AuthorizationSchema

authorization_schema = AuthorizationSchema()
authorizations_schema = AuthorizationSchema(many=True)

class AuthorizationResource(Resource):
    def get(self, authorization_id):
        authorization = Authorization.query.get_or_404(authorization_id)
        return authorization_schema.dump(authorization)

    def put(self, authorization_id):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int)
        parser.add_argument('role', type=str)
        parser.add_argument('last_login', type=str)

        args = parser.parse_args()

        authorization = Authorization.query.get_or_404(authorization_id)
        

        authorization.user_id = args['user_id'] or authorization.user_id
        authorization.role = args['role'] or authorization.role
        authorization.last_login = args['last_login'] or authorization.last_login

        db.session.commit()

        return authorization_schema.dump(authorization)

    def delete(self, authorization_id):
        authorization = Authorization.query.get_or_404(authorization_id)
        db.session.delete(authorization)
        db.session.commit()
        return {'message': 'Authorization deleted successfully'}

class AuthorizationsResource(Resource):
    def get(self):
        authorizations = Authorization.query.all()
        return authorizations_schema.dump(authorizations)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('role', type=str, required=True)
        parser.add_argument('last_login', type=str)

        args = parser.parse_args()

        new_authorization = Authorization(user_id=args['user_id'], role=args['role'], last_login=args['last_login'])
        db.session.add(new_authorization)
        db.session.commit()

        return authorization_schema.dump(new_authorization), 201
