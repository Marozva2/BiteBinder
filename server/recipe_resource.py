from flask_restful import Resource, reqparse
from models import db, Recipe
from schema import RecipeSchema
from flask import jsonify

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

class RecipeResource(Resource):
    def get(self, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        return jsonify(recipe_schema.dump(recipe))

    def put(self, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        args = parser.parse_args()

        # Update recipe attributes
        recipe.title = args['title'] or recipe.title
        recipe.description = args['description'] or recipe.description

        db.session.commit()
        return jsonify(recipe_schema.dump(recipe))

    def delete(self, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
        return '', 204

class RecipesResource(Resource):
    def get(self):
        recipes = Recipe.query.all()
        return jsonify(recipes_schema.dump(recipes))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('user_id', type=int, required=True)
        args = parser.parse_args()

        new_recipe = Recipe(title=args['title'], description=args['description'], user_id=args['user_id'])
        db.session.add(new_recipe)
        db.session.commit()
        return jsonify(recipe_schema.dump(new_recipe)), 201
