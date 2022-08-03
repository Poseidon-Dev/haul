from sqlalchemy import Column, String, Integer, Boolean
from marshmallow import Schema
from database import Base, db
from models.base import BaseModel


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

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.is_active

    def __repr__(self):
        return f'<User {self.name}'
    