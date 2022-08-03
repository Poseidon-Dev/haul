from sqlalchemy import Column, String, Integer, Boolean
from marshmallow import Schema
from database import Base
import config


class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer(), unique=True, primary_key=True)
    position = Column(String(25))
    
    def __init__(self, position_number):

        self.id = position_number
        self.position = self.get_position(position_number)

    def get_position(self, id):
        return config.POSITIONS.get(id, 'Unknown')

class PositionSchema(Schema):
    class meta:
        fields = ('position')
        model = Position

_positions = PositionSchema(many=True)