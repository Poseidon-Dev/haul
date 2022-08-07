from ast import Eq
from flask_login import (
    current_user,
)
from flask_restful import Api, Resource

from core.settings.database import db
from core.models import Equipment, Profile, User, EquipmentQueue
from core.models import _equips, _profile, _user, _equip_queues
from core.views.utils import CurrentUser

def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Division: {}</p>"
            "<div><p>Position: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile.division, current_user.profile.position, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'

def db_test():
    user = CurrentUser('12345')
    e = Equipment.query.filter(Equipment.division_id==user._profile.division_id)
    eq = EquipmentQueue.query.filter(EquipmentQueue.user_id==user._profile.user_id)
    resp = {
        'user': user.user,
        'profile': user.profile,
        'equipment': _equips.dump(e),
        'equipment_queue': _equip_queues.dump(eq),
    }
    return resp

class EquipmentListResource(Resource):
    def get(self):
        equips = Equipment.query.all()
        return _equips.dump(equips)
