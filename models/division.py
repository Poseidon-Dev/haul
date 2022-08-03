from sqlalchemy import Column, String, Integer, Boolean
from database import Base
import config

class Division(Base):
    __tablename__ = 'division'

    id = Column(Integer(), unique=True, primary_key=True)
    division = Column(String(25))
    
    def __init__(self, division_number):
        self.id = division_number
        self.division = self.get_division(division_number)

    def get_division(self, id):
        return config.DIVISIONS.get(id, 'Unknown')