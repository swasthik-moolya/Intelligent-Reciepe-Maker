from flask import Flask, render_template, request, jsonify
from models import db, Ingredient, Recipe, Rating

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    ingredient = request.form.get('ingredient')
    new_ingredient = Ingredient(name=ingredient)
    db.session.add(new_ingredient)
    db.session.commit()
    return jsonify({"message": "Ingredient added successfully"}), 200


@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    # Placeholder for actual recipe retrieval logic
    recipes = [
        {"name": "Pasta Primavera", "instructions": "Boil pasta. Stir-fry vegetables. Mix together."},
        {"name": "Veggie Stir-fry", "instructions": "Stir-fry vegetables. Serve with rice."}
    ]
    return jsonify(recipes), 200


@app.route('/rate_recipe', methods=['POST'])
def rate_recipe():
    recipe_id = request.form.get('recipe_id')
    rating = request.form.get('rating')
    feedback = request.form.get('feedback')
    new_rating = Rating(recipe_id=recipe_id, rating=rating, feedback=feedback)
    db.session.add(new_rating)
    db.session.commit()
    return jsonify({"message": "Feedback submitted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
