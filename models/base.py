from sqlalchemy import Column, String
from sqlalchemy.exc import NoResultFound
from uuid import uuid4
from database import db

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
