from sqlalchemy import Column, String, Integer, Boolean
from marshmallow import Schema
from core.models.account import User
from core.settings.database import Base
from core.models.base import BaseModel
from core.models.division import Division

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

_equip = EquipmentSchema()
_equips = EquipmentSchema(many=True)

class EquipmentQueue(Base, BaseModel):

    __tablename__ = 'equipment_queue'

    equipment_id = Column(String(10))
    user_id = Column(String(36), unique=True)
    from_division = Column(Integer())
    to_division = Column(Integer())
    issue_date = Column(String(10))
    accepted_date = Column(String(10))
    completed_date = Column(String(10))
    status = Column(Integer())

    def __init__(self, equipment_id, user_id, from_division, to_division, issue_date, status=1, accepted_date=None, completed_date=None):
        self.equipment_id = equipment_id
        self.user_id = user_id
        self.from_division = from_division
        self.to_division = to_division
        self.issue_date = issue_date
        self.accepted_date = accepted_date
        self.completed_date = completed_date
        self.status = status

    @property
    def equipment(self):
        return self.get_related_obj(Equipment, Equipment.equipment_id, self.equipment_id)

    @property
    def user(self):
        return self.get_related_obj(User, User.id, self.user_id)

class EquipmentQueueSchema(Schema):
    class Meta:
        fields = ('equipment_id', 'from_division', 'to_division', 'issue_date', 'accepted_date', 'completed_date')
        model = EquipmentQueue

_equip_queue = EquipmentQueueSchema()
_equip_queues = EquipmentQueueSchema(many=True)