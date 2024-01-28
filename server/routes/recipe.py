from flask_restful import Resource, reqparse
from models import db, Recipe
from schema import RecipeSchema
from flask import jsonify
import requests

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

apiKey = 'a0fb34d2e4204a8a9ae9e15588519efc'

class RecipeResource(Resource):
    def get(self, recipe_id):
        response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={apiKey}')
        data = response.json()
        recipe = Recipe(title=data['title'], description=data['instructions'])
        return jsonify(recipe_schema.dump(recipe))

    def put(self, recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        args = parser.parse_args()

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
        response = requests.get(f'https://api.spoonacular.com/recipes/complexSearch?apiKey={apiKey}')
        data = response.json()
        recipes = [Recipe(title=recipe['title'], description=recipe['instructions']) for recipe in data['results']]
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
