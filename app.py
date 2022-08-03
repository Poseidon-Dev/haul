from flask import Flask
import views
from views.auth import login_manager
from database import init_db
import config
from flask_restful import Api
from views.index import EquipmentListResource

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


if __name__ == "__main__":
    # app.run(ssl_context="adhoc", debug=True)
    app.run(debug=True)