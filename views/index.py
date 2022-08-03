from flask_login import (
    current_user,
)

from database import db
from models import User

def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Division: {}</p>"
            "<div><p>Position: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile, current_user.profile, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'

def db_test():
    q = db.query(User)
    user = q.filter(User.id=='104254980911636950356').one()
    resp = {
        'user': user.as_dict(),
        'profile': user.profile.as_dict()
    }
    return resp