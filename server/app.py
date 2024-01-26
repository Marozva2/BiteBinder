from flask import Flask
from flask_restful import Api
from models import db
from flask_migrate import Migrate 

# Import the resource classes
from user_resource import UserResource, UsersResource
from profile_resource import ProfileResource, ProfilesResource
from recipe_resource import RecipeResource, RecipesResource
from instruction_resource import RecipeInstructionsResource, RecipeInstructionsListResource
from ingredient_resource import RecipeIngredientResource, RecipeIngredientsResource
from review_resource import ReviewResource, ReviewsResource
from favourites_resource import FavoritesResource, FavoritesListResource
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'm3BCV7djD1RxeFn0bdzlP-3lqVh0tQsTc-Oc9PyLYMs'

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)
CORS(app)

api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(UsersResource, '/users')

api.add_resource(ProfileResource, '/profile/<int:profile_id>')
api.add_resource(ProfilesResource, '/profiles')

api.add_resource(RecipeResource, '/recipe/<int:recipe_id>')
api.add_resource(RecipesResource, '/recipes')

api.add_resource(RecipeInstructionsResource, '/instruction/<int:instruction_id>')
api.add_resource(RecipeInstructionsListResource, '/instructions')

api.add_resource(RecipeIngredientResource, '/ingredient/<int:ingredient_id>')
api.add_resource(RecipeIngredientsResource, '/ingredients')

api.add_resource(ReviewResource, '/review/<int:review_id>')
api.add_resource(ReviewsResource, '/reviews')  

api.add_resource(FavoritesResource, '/favorite/<int:favorite_id>')
api.add_resource(FavoritesListResource, '/favorites')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
