from flask_restful import Resource, reqparse
from models import db, RecipeInstructions
from schema import RecipeInstructionsSchema
from flask import jsonify
import requests

recipe_instructions_schema = RecipeInstructionsSchema()
recipe_instructions_list_schema = RecipeInstructionsSchema(many=True)

apiKey = 'a0fb34d2e4204a8a9ae9e15588519efc'

class RecipeInstructionsResource(Resource):
    def get(self, instruction_id):
        response = requests.get(f'https://api.spoonacular.com/recipes/{instruction_id}/analyzedInstructions?apiKey={apiKey}')
        data = response.json()
        instruction = RecipeInstructions(detail=data[0]['steps'][0]['step'])
        return jsonify(recipe_instructions_schema.dump(instruction))

    def put(self, instruction_id):
        instruction = RecipeInstructions.query.get_or_404(instruction_id)
        parser = reqparse.RequestParser()
        parser.add_argument('detail', type=str)
        args = parser.parse_args()

        instruction.detail = args['detail'] or instruction.detail

        db.session.commit()
        return jsonify(recipe_instructions_schema.dump(instruction))

    def delete(self, instruction_id):
        instruction = RecipeInstructions.query.get_or_404(instruction_id)
        db.session.delete(instruction)
        db.session.commit()
        return '', 204

class RecipeInstructionsListResource(Resource):
    def get(self):
        response = requests.get(f'https://api.spoonacular.com/recipes/complexSearch?apiKey={apiKey}')
        data = response.json()
        instructions = [RecipeInstructions(detail=recipe['title']) for recipe in data['results']]
        return jsonify(recipe_instructions_list_schema.dump(instructions))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('recipe_id', type=int, required=True)
        parser.add_argument('detail', type=str, required=True)
        args = parser.parse_args()

        new_instruction = RecipeInstructions(recipe_id=args['recipe_id'], detail=args['detail'])
        db.session.add(new_instruction)
        db.session.commit()
        return jsonify(recipe_instructions_schema.dump(new_instruction)), 201
