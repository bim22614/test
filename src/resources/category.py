import uuid
from flask import jsonify, request
from src import app, db
from src.models import CategoryModel
from src.schemas import CategorySchema
from marshmallow import ValidationError

category_schema = CategorySchema()


@app.get('/category')
def get_category():
    categories = CategoryModel.query.all()
    return jsonify(category_schema.dump(categories, many=True)), 200


@app.post('/category')
def create_category():
    category_data = request.get_json()
    try:
        data = category_schema.load(category_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    data['id'] = str(uuid.uuid4())
    category = CategoryModel(**data)
    try:
        db.session.add(category)
        db.session.commit()
    except Exception as e:
        return jsonify(error=str(e)), 400
    return jsonify(category)


@app.delete('/category/<category_id>')
def delete_category(category_id):
    if not uuid.UUID(category_id, version=4):
        return jsonify({"error": "Invalid category_id format"}), 400

    category = CategoryModel.query.get(category_id)
    try:
        db.session.delete(category)
        db.session.commit()
        return jsonify(category_schema.dump(category)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
