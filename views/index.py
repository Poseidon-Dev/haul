from ast import Eq
from flask_login import (
    current_user,
)
from flask_restful import Api, Resource

from database import db
from models import Equipment, Profile, User
from models import _equips, _profile, _user

def dummy_equip():
    e = Equipment('12345', 'Test Equipment', '12321', 'Truck', '2019', 4, 11, 110, '300000', '32', division_id=0)
    db.add(e)
    e = Equipment('12345', 'Test Equipment 2', '12221', 'Truck', '2019', 4, 11, 110, '300000', '32')
    db.add(e)
    e = Equipment('12245', 'Test Equipment 3', '123221', 'Truck', '2019', 4, 11, 110, '300000', '32')
    db.add(e)
    e = Equipment('12315', 'Test Equipment 4', '123231', 'Truck', '2019', 4, 11, 110, '300000', '32')
    db.add(e)
    db.commit()

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
    # dummy_equip()
    u = User.query.filter(User.id=='104254980911636950356').one()
    p = Profile.query.filter(Profile.user_id==u.id).one()
    e = Equipment.query.filter(Equipment.division_id==p.division_id)
    resp = {
        'user': _user.dump(u),
        'profile': _profile.dump(p),
        'equip': _equips.dump(e),
    }
    return resp

class EquipmentListResource(Resource):
    def get(self):
        equips = Equipment.query.all()
        return _equips.dump(equips)
