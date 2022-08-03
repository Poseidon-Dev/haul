from sqlalchemy import Column, String, Integer, Boolean
from marshmallow import Schema
from database import Base
from models.base import BaseModel
from models.division import Division

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