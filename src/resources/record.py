import uuid
from flask import jsonify, request
from src import app, db
from datetime import datetime
from src.models import RecordModel, UserModel, CategoryModel
from src.schemas import RecordSchema
from marshmallow import ValidationError

record_schema = RecordSchema()


@app.get('/record/<record_id>')
def get_record(record_id):
    record = RecordModel.query.get(record_id)
    try:
        return jsonify(record_schema.dump(record)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400



@app.delete('/record/<record_id>')
def delete_record(record_id):
    record = RecordModel.query.get(record_id)
    try:
        db.session.delete(record)
        db.session.commit()
        return jsonify(record_schema.dump(record)), 200
    except ValidationError as err:
        return jsonify(err.messages), 400



@app.post('/record')
def create_record():
    record_data = request.args
    try:
        data = record_schema.load(record_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    data['id'] = uuid.uuid4().hex
    data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = UserModel.query.get(record_data['user_id'])
    category = CategoryModel.query.get(record_data["category_id"])
    if (user and category):
        data["user_id"] = user.id
        data["category_id"] = category.id
        record = RecordModel(**data)
    else:
        return "Incorrect record data", 400
    try:
        db.session.add(record)
        db.session.commit()
    except Exception as e:
        return jsonify(error=str(e)), 400
    return jsonify(record), 200


@app.get('/record')
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')

    if user_id is None and category_id is None:
        return "Missing parameters", 400

    query = RecordModel.query
    if user_id is not None:
        query = query.filter_by(user_id=user_id)
    if category_id is not None:
        query = query.filter_by(category_id=category_id)

    try:
        records = query.all()
    except Exception as e:
        return jsonify(error=str(e)), 400

    return jsonify(record_schema.dump(records, many=True)), 200