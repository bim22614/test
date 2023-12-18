import uuid
from flask import jsonify, request
from src import app
from datetime import datetime

records = {}


@app.get('/record/<record_id>')
def get_record(record_id):
    if record_id not in records:
        return jsonify(error=f'Record with {record_id} id does not exist'), 404
    else:
        record = records[record_id]
        return jsonify(record)


@app.delete('/record/<record_id>')
def delete_record(record_id):
    if record_id not in records:
        return jsonify(error=f'Record with {record_id} id does not exist'), 404
    else:
        del records[record_id]
        return jsonify(f"Record deleted by {record_id} id")


@app.post('/record')
def create_record():
    record_id = uuid.uuid4().hex
    user_id = request.args.get("user_id")
    category_id = request.args.get("category_id")
    created_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cost_amount = request.args.get("cost_amount")
    record = {
        "record_id": record_id,
        "user_id": user_id,
        "category_id": category_id,
        "created_time": created_time,
        "cost_amount": cost_amount
    }
    records[record_id] = record
    return jsonify(record)


@app.get('/record')
def get_records():
    user_id = request.args.get("user_id")
    category_id = request.args.get("category_id")

    if not user_id and not category_id:
        return jsonify(error='Both user_id and category_id are required'), 400

    filtered_records = [record for record in records.values() if
                        (not user_id or record['user_id'] == user_id) and
                        (not category_id or record['category_id'] == category_id)]

    return jsonify({'data': filtered_records})