from flask_restful import Resource
from flask import jsonify
from core.models import Equipment, _equips
from core.settings.database import db

class EquipmentApi(Resource):

    def post(self):
        print('Received Request')
        eq = Equipment('12345', '12345', 1, 2, '20220807')
        db.add(eq)
        db.commit()

    def get(self):
        e = Equipment.query.all()
        return jsonify(_equips.dump(e))
        