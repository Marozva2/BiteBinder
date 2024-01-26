from flask_restful import Resource, reqparse
from models import db, RecipeInstructions
from schema import RecipeInstructionsSchema
from flask import jsonify

recipe_instructions_schema = RecipeInstructionsSchema()
recipe_instructions_list_schema = RecipeInstructionsSchema(many=True)

class RecipeInstructionsResource(Resource):
    def get(self, instruction_id):
        instruction = RecipeInstructions.query.get_or_404(instruction_id)
        return jsonify(recipe_instructions_schema.dump(instruction))

    def put(self, instruction_id):
        instruction = RecipeInstructions.query.get_or_404(instruction_id)
        parser = reqparse.RequestParser()
        parser.add_argument('detail', type=str)
        args = parser.parse_args()

        # Update instruction attributes
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
        instructions = RecipeInstructions.query.all()
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
