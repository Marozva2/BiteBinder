from flask_restful import Resource, reqparse
from models import db, Profile
from schema import ProfileSchema
from flask import jsonify

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)

class ProfileResource(Resource):
    def get(self, profile_id):
        profile = Profile.query.get_or_404(profile_id)
        return jsonify(profile_schema.dump(profile))

    def put(self, profile_id):
        profile = Profile.query.get_or_404(profile_id)
        parser = reqparse.RequestParser()
        parser.add_argument('firstname', type=str)
        parser.add_argument('lastname', type=str)
        parser.add_argument('image_url', type=str)
        args = parser.parse_args()

        # Update profile attributes
        profile.firstname = args['firstname'] or profile.firstname
        profile.lastname = args['lastname'] or profile.lastname
        profile.image_url = args['image_url'] or profile.image_url

        db.session.commit()
        return jsonify(profile_schema.dump(profile))

    def delete(self, profile_id):
        profile = Profile.query.get_or_404(profile_id)
        db.session.delete(profile)
        db.session.commit()
        return '', 204

class ProfilesResource(Resource):
    def get(self):
        profiles = Profile.query.all()
        return jsonify(profiles_schema.dump(profiles))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstname', type=str, required=True)
        parser.add_argument('lastname', type=str, required=True)
        parser.add_argument('image_url', type=str)
        parser.add_argument('user_id', type=int, required=True)
        args = parser.parse_args()

        new_profile = Profile(firstname=args['firstname'], lastname=args['lastname'], image_url=args['image_url'], user_id=args['user_id'])
        db.session.add(new_profile)
        db.session.commit()
        return jsonify(profile_schema.dump(new_profile)), 201
