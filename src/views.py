import uuid
from flask import jsonify, request
from src import app
from datetime import datetime

users = {}
categories = {}
records = {}


@app.get('/healthcheck')
def healthcheck():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    health_status = {'status': 'OK', 'date': current_date}
    return jsonify(health_status)


@app.get('/user/<user_id>')
def get_user(user_id):
    if user_id not in users:
        return jsonify(error=f'User with {user_id} id does not exist'), 404
    else:
        user = users[user_id]
        return jsonify(user)


@app.delete('/user/<user_id>')
def delete_user(user_id):
    if user_id not in users:
        return jsonify(error=f'User with {user_id} id does not exist'), 404
    else:
        del users[user_id]
        return f"User deleted by {user_id} id"


@app.post('/user')
def create_user():
    user_name = request.args.get("name")
    user_id = uuid.uuid4().hex
    user = {"id": user_id, "name": user_name}
    users[user_id] = user
    return jsonify(user)


@app.get('/users')
def get_users():
    return list(users.values())


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


if __name__ == '__main__':
    app.run(debug=True)
