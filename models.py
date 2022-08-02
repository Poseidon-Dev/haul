from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class User(Base):

    __tablename__ = 'user'

    id = Column(String(50), primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(50), unique=False)
    profile_pic = Column(String(255))
    domain = Column(String(50), unique=False)
    is_active = Column(Boolean())

    def __init__(self, id, name, email, profile_pic, domain, is_active):
        self.id = id
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.domain = domain
        self.is_active = is_active

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.is_active

    def __repr__(self):
        return f'<User {self.name}'

