from flask import Flask
import core.views as views
from core.views.auth import login_manager
from core.settings.database import init_db
import core.settings.config as config
from core.views.index import EquipmentListResource
from core.views.equipment import EquipmentQueueApi
from flask_restful import Api

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

init_db()
login_manager.init_app(app)

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/test', view_func=views.db_test)
app.add_url_rule('/login', view_func=views.login)
app.add_url_rule('/login/callback', view_func=views.callback)
app.add_url_rule('/logout', view_func=views.logout)


Api(app).add_resource(EquipmentListResource, '/equip')
Api(app).add_resource(EquipmentQueueApi, '/queue')


if __name__ == "__main__":
    # app.run(ssl_context="adhoc", debug=True)
    app.run(debug=True)