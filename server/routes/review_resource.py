from flask_restful import Resource, reqparse
from models import db, Review
from schema import ReviewSchema
from flask import jsonify

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

class ReviewResource(Resource):
    def get(self, review_id):
        review = Review.query.get_or_404(review_id)
        return jsonify(review_schema.dump(review))

    def put(self, review_id):
        review = Review.query.get_or_404(review_id)
        parser = reqparse.RequestParser()
        parser.add_argument('rating', type=int)
        parser.add_argument('comment', type=str)
        args = parser.parse_args()

        # Update review attributes
        review.rating = args['rating'] or review.rating
        review.comment = args['comment'] or review.comment

        db.session.commit()
        return jsonify(review_schema.dump(review))

    def delete(self, review_id):
        review = Review.query.get_or_404(review_id)
        db.session.delete(review)
        db.session.commit()
        return '', 204

class ReviewsResource(Resource):
    def get(self):
        reviews = Review.query.all()
        return jsonify(reviews_schema.dump(reviews))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('rating', type=int, required=True)
        parser.add_argument('comment', type=str, required=True)
        parser.add_argument('user_id', type=int, required=True)
        parser.add_argument('recipe_id', type=int, required=True)
        args = parser.parse_args()

        new_review = Review(rating=args['rating'], comment=args['comment'], user_id=args['user_id'], recipe_id=args['recipe_id'])
        db.session.add(new_review)
        db.session.commit()
        return jsonify(review_schema.dump(new_review)), 201
