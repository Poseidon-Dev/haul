from sqlalchemy import Column, String, Integer, Boolean
from marshmallow import Schema
from core.settings.database import Base
from core.models.base import BaseModel
from core.models.division import Division
from core.models.position import Position


class User(Base, BaseModel):

    __tablename__ = 'user'

    uuid = Column(String(36), unique=True, primary_key=True, )
    id = Column(String(50))
    first_name = Column(String(50), unique=False)
    last_name = Column(String(50), unique=False)
    email = Column(String(50), unique=False)
    profile_pic = Column(String(255))
    domain = Column(String(50), unique=False)
    is_active = Column(Boolean())

    def __init__(self, id, first_name, last_name, email, profile_pic, domain, is_active):
        self.uuid = self._uuid
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.profile_pic = profile_pic
        self.domain = domain
        self.is_active = is_active
        super(User, self).__init__()

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def profile(self):
        return self.get_related_obj(Profile, Profile.user_id, self.id)

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.is_active

    def __repr__(self):
        return f'<User {self.name}'
    
class UserSchema(Schema):
    class Meta:
        fields = ('uuid', 'is_active', 'domain')
        model = User

_user = UserSchema()
_users = UserSchema(many=True)

class Profile(Base, BaseModel):

    __tablename__ = 'profile'

    user_id = Column(String(36), unique=True)
    division_id = Column(Integer())
    position_is = Column(Integer())

    def __init__(self, user_id, division_id=99, position_id=99):
        self.uuid = self._uuid
        self.user_id = user_id
        self.division_id = division_id
        self.position_id = position_id
        super(Profile, self).__init__()

    @property
    def user(self):
        return self.get_related_obj(User, User.id, self.user_id)

    @property
    def division(self):
        return self.get_related_obj(Division, Division.id, self.division_id).division

    @property
    def position(self):
        return self.get_related_obj(Position, Position.id, self.position_id).position

class ProfileSchema(Schema):
    class Meta:
        fields = ('user.name', 'division', 'position', 'user.email', 'user.profile_pic')
        model = Profile

_profile = ProfileSchema()
_profiles = ProfileSchema(many=True)