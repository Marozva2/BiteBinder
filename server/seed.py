# seed.py

from faker import Faker
from models import db, User, Profile, Review, Recipe, RecipeIngredient, RecipeInstructions, Favorites
from app import app
import random

fake = Faker()

# Create all tables
with app.app_context():
    db.create_all()

# Add seed data
with app.app_context():
    for _ in range(10):
        # Create a fake user
        user = User(username=fake.user_name(), email=fake.email(), password=fake.password(), created_at=fake.date_time_this_year())
        db.session.add(user)
        db.session.commit()  # Commit immediately after adding the user

        # Create a fake profile for the user
        profile = Profile(firstname=fake.first_name(), lastname=fake.last_name(), image_url=fake.image_url(), user_id=user.id)
        db.session.add(profile)
        db.session.commit()  # Commit immediately after adding the profile

        # Create some fake recipes for the user
        for _ in range(random.randint(1, 5)):
            recipe = Recipe(title=fake.sentence(), description=fake.paragraph(), user_id=user.id, created_at=fake.date_time_this_year())
            db.session.add(recipe)
            db.session.commit()  # Commit immediately after adding the recipe

            # Create some fake reviews for the recipe
            for _ in range(random.randint(1, 5)):
                review = Review(rating=random.randint(1, 5), comment=fake.paragraph(), user_id=user.id, recipe_id=recipe.id, created_at=fake.date_time_this_year())
                db.session.add(review)

            # Create some fake instructions for the recipe
            for _ in range(random.randint(1, 5)):
                instruction = RecipeInstructions(recipe_id=recipe.id, detail=fake.sentence())
                db.session.add(instruction)

            # Create some fake ingredients for the recipe
            for _ in range(random.randint(1, 5)):
                ingredient = RecipeIngredient(recipe_id=recipe.id, quantity=fake.random_element(elements=('1 cup', '2 tbsp', '1/2 tsp')), name=fake.word(), created_at=fake.date_time_this_year())
                db.session.add(ingredient)

            # Add the recipe to favorites
            if random.choice([True, False]):
                favorite = Favorites(user_id=user.id, recipe_id=recipe.id, created_at=fake.date_time_this_year())
                db.session.add(favorite)

    db.session.commit()
