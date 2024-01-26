from flask_restful import Resource, reqparse
from models import db, Favorites
from schema import FavoritesSchema
from flask import jsonify

favorites_schema = FavoritesSchema()
favorites_list_schema = FavoritesSchema(many=True)

class FavoritesResource(Resource):
    def get(self, favorite_id):
        favorite = Favorites.query.get_or_404(favorite_id)
        return jsonify(favorites_schema.dump(favorite))

    def delete(self, favorite_id):
        favorite = Favorites.query.get_or_404(favorite_id)
        db.session.delete(favorite)
        db.session.commit()
        return '', 204

class FavoritesListResource(Resource):
    def get(self):
        favorites = Favorites.query.all()
        return jsonify(favorites_list_schema.dump(favorites))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('recipe_id', type=int, required=True)
        args = parser.parse_args()

        new_favorite = Favorites(user_id=args['user_id'], recipe_id=args['recipe_id'])
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify(favorites_schema.dump(new_favorite)), 201
