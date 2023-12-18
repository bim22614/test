import uuid
from flask import jsonify, request
from src import app

categories = {}


@app.get('/category')
def get_category():
    return list(categories.values())


@app.post('/category')
def create_category():
    category_name = request.args.get("name")
    category_id = uuid.uuid4().hex
    category = {"id": category_id, "name": category_name}
    categories[category_id] = category
    return jsonify(category)


@app.delete('/category/<category_id>')
def delete_category(category_id):
    if category_id not in categories:
        return jsonify(error=f'Category with {category_id} id does not exist'), 404
    else:
        del categories[category_id]
        return f"Category deleted by {category_id} id"
