import os

import views
from views.auth import login_manager
from database import init_db

from flask import Flask

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

init_db()
login_manager.init_app(app)

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/login', view_func=views.login)
app.add_url_rule('/login/callback', view_func=views.callback)
app.add_url_rule('/logout', view_func=views.logout)

if __name__ == "__main__":
    app.run(ssl_context="adhoc")