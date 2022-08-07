from flask_restful import Resource
from core.models import EquipmentQueue, _equip_queues, Equipment
from core.settings.database import db

class EquipmentQueueApi(Resource):

    def post(self):
        eq = EquipmentQueue('12345', '12345', 1, 2, '20220807')
        db.add(eq)
        db.commit()

    def get(self):
        e = EquipmentQueue.query.all()
        return {
            'queue': _equip_queues.dump(e)
        }