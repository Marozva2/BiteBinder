from flask_restful import Resource, reqparse
from models import db, RecipeIngredient
from schema import RecipeIngredientSchema
from flask import jsonify

recipe_ingredient_schema = RecipeIngredientSchema()
recipe_ingredients_schema = RecipeIngredientSchema(many=True)

class RecipeIngredientResource(Resource):
    def get(self, ingredient_id):
        ingredient = RecipeIngredient.query.get_or_404(ingredient_id)
        return jsonify(recipe_ingredient_schema.dump(ingredient))

    def put(self, ingredient_id):
        ingredient = RecipeIngredient.query.get_or_404(ingredient_id)
        parser = reqparse.RequestParser()
        parser.add_argument('quantity', type=str)
        parser.add_argument('name', type=str)
        args = parser.parse_args()

        # Update ingredient attributes
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
        ingredients = RecipeIngredient.query.all()
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
