from flask_restful import Resource, reqparse
from models import db, RecipeIngredient
from schema import RecipeIngredientSchema
from flask import jsonify
import requests

recipe_ingredient_schema = RecipeIngredientSchema()
recipe_ingredients_schema = RecipeIngredientSchema(many=True)

apiKey = 'a0fb34d2e4204a8a9ae9e15588519efc'

class RecipeIngredientResource(Resource):
    def get(self, ingredient_id):
        response = requests.get(f'https://api.spoonacular.com/food/ingredients/{ingredient_id}/information?apiKey={apiKey}')
        data = response.json()
        ingredient = RecipeIngredient(quantity=data['amount'], name=data['name'])
        return jsonify(recipe_ingredient_schema.dump(ingredient))

    def put(self, ingredient_id):
        ingredient = RecipeIngredient.query.get_or_404(ingredient_id)
        parser = reqparse.RequestParser()
        parser.add_argument('quantity', type=str)
        parser.add_argument('name', type=str)
        args = parser.parse_args()

        ingredient.quantity = args['quantity'] or ingredient.quantity
        ingredient.name = args['name'] or ingredient.name

        db.session.commit()
        return jsonify(recipe_ingredient_schema.dump(ingredient))

    def delete(self, ingredient_id):
        ingredient = RecipeIngredient.query.get_or_404(ingredient_id)
        db.session.delete(ingredient)
        db.session.commit()
        return '', 204

class RecipeIngredientsResource(Resource):
    def get(self):
        response = requests.get(f'https://api.spoonacular.com/recipes/complexSearch?apiKey={apiKey}')
        data = response.json()
        ingredients = [RecipeIngredient(quantity=ingredient['amount'], name=ingredient['name']) for ingredient in data['results'][0]['usedIngredients']]
        return jsonify(recipe_ingredients_schema.dump(ingredients))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('recipe_id', type=int, required=True)
        parser.add_argument('quantity', type=str, required=True)
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        new_ingredient = RecipeIngredient(recipe_id=args['recipe_id'], quantity=args['quantity'], name=args['name'])
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify(recipe_ingredient_schema.dump(new_ingredient)), 201
