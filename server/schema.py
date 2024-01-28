from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import User, Review, Profile, RecipeInstructions, RecipeIngredient, Recipe, Favorites, Authorization

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

class ReviewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Review

class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile

class RecipeInstructionsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeInstructions

class RecipeIngredientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RecipeIngredient

class FavoritesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Favorites

class AuthorizationSchema(SQLAlchemyAutoSchema):
    user = fields.Nested(UserSchema)

    class Meta:
        model = Authorization

class RecipeSchema(SQLAlchemyAutoSchema):
    reviews = fields.Nested(ReviewSchema, many=True)
    recipe_instructions = fields.Nested(RecipeInstructionsSchema, many=True)
    recipe_ingredients = fields.Nested(RecipeIngredientSchema, many=True)
    favorites = fields.Nested(FavoritesSchema, many=True)

    class Meta:
        model = Recipe
