from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.exc import NoResultFound
from marshmallow import Schema
from database import Base, db
from uuid import uuid4
import config

class BaseModel:

    uuid = Column(String(36), unique=True, primary_key=True)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @property
    def _uuid(self):
        return str(uuid4())

    @staticmethod
    def get_related_obj(obj, obj_id, id):
        q = db.query(obj)
        try:
            resp = q.filter(obj_id==id).one()
            return resp
        except NoResultFound:
            return None


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
    

class Division(Base):
    __tablename__ = 'division'

    id = Column(Integer(), unique=True, primary_key=True)
    division = Column(String(25))
    
    def __init__(self, division_number):
        self.id = division_number
        self.division = self.get_division(division_number)

    def get_division(self, id):
        return config.DIVISIONS.get(id, 'Unknown')

class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer(), unique=True, primary_key=True)
    position = Column(String(25))
    
    def __init__(self, position_number):

        self.id = position_number
        self.position = self.get_position(position_number)

    def get_position(self, id):
        return config.POSITIONS.get(id, 'Unknown')

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
    def get_position(self):
        return self.get_related_obj(Position, Position.id, self.position_id).position

class Equipment(Base, BaseModel):

    __tablename__ = 'equipment'

    equipment_id = Column(String(10))
    description = Column(String(100))
    description2 = Column(String(100))
    description3 = Column(String(100))
    serial = Column(String(25))
    model = Column(String(25))
    model_year = Column(Integer())
    status_code = Column(Integer())
    department = Column(Integer())
    item_class = Column(Integer())
    job_number = Column(String(10))
    warehouse = Column(String(10))
    division_id = Column(Integer())

    def __init__(
                self, 
                equipment_id, 
                description, 
                serial,
                model,
                model_year,
                status_code,
                department,
                item_class,
                job_number,
                warehouse,
                description2=None, 
                description3=None, 
                division_id=99):
        self.uuid = self._uuid
        self.equipment_id = equipment_id
        self.description = description
        self.description2 = description2
        self.description3 = description3
        self.serial = serial
        self.model = model
        self.model_year = model_year
        self.status_code = status_code
        self.department = department
        self.item_class = item_class
        self.job_number = job_number
        self.warehouse = warehouse
        self.division_id = division_id
        super(Equipment, self).__init__()

    @property
    def division(self):
        return self.get_related_obj(Division, Division.id, self.division_id).division

class EquipmentSchema(Schema):
    class Meta:
        fields = ('equipment_id', 'description', 'division', 'division_id')
        model = Equipment

equipments_schema = EquipmentSchema(many=True)