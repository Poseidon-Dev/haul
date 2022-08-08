from flask_restful import Resource
from flask import request, abort, Response
from core.models import EquipmentQueue, _equip_queues, _equip_queue
from core.models import Equipment, _equips, _equip
from core.settings.database import db

class EquipmentQueueApi(Resource):

    def post(self):
        post = request.get_json()
        for p in post:
            try:
                getattr(EquipmentQueue, p)
            except AttributeError:
                return 'Bad Request', 400
        e = Equipment.query.filter(Equipment.equipment_id==post['equipment_id']).first()
        if not e:
            return Response(f'Equipment {post["equipment_id"]} is not available for queue', 400)

        eq = EquipmentQueue(
            e.equipment_id,
            post['user_id'],
            e.division_id,
            post['to_division'],
            post['issue_date']
        )
        db.delete(e)
        db.add(eq)
        db.commit()
        
        return _equip.dump(e)

        eq = EquipmentQueue(
            post['equipment_id'], 
            post['user_id'],
            post['from_division'],
            post['to_division'],
            post['issue_date'],
            )
        db.add(eq)
        db.commit()
        return _equip_queue.dump(eq)

    def get(self):
        e = EquipmentQueue.query.all()
        return {
            'queue': _equip_queues.dump(e)
        }