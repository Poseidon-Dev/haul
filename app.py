from flask import Flask
from flask_cors import CORS, cross_origin
import core.api as api
from core.api.auth import login_manager
from core.settings.database import init_db
import core.settings.config as config
from core.api.equipment import EquipmentQueueApi, EquipmentApi
from flask_restful import Api

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

init_db()
login_manager.init_app(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.add_url_rule('/', view_func=api.index)
app.add_url_rule('/test', view_func=api.db_test)
app.add_url_rule('/login', view_func=api.login)
app.add_url_rule('/login/callback', view_func=api.callback)
app.add_url_rule('/logout', view_func=api.logout)

_api = Api(app)
# Api(app).add_resource(EquipmentListResource, '/equip')
Api(app).add_resource(EquipmentQueueApi, '/queue')
Api(app).add_resource(EquipmentApi, '/equip')


if __name__ == "__main__":
    # app.run(ssl_context="adhoc", debug=True)
    app.run(debug=True, host='0.0.0.0')