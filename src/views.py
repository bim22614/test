from flask import jsonify, Blueprint
#from src import app
from datetime import datetime


blueprint = Blueprint(name='healthcheck', import_name=__name__)


@blueprint.get('/healthcheck')
def healthcheck():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    health_status = {'status': 'OK', 'date': current_date}
    return jsonify(health_status)
