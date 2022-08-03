from sqlalchemy import Column, String, Integer, Boolean
from marshmallow import Schema
from database import Base
from models.base import BaseModel
from models.division import Division
from models.position import Position
from models.user import User

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