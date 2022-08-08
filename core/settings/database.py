import os
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base

import core.settings.config as config



if config.ENVIRONMENT == 'development':
    try:
        print(f'{config.DB_PATH}{config.DB_NAME}')
        os.remove(f'{config.BASE_DIR}/data/{config.DB_NAME}')
    except Exception as e:
        print(e)
        print('Building DB')

try:
    engine = create_engine(f'sqlite:////{config.DB_PATH}{config.DB_NAME}')
except Exception as e:
    print(e)


db = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
Base.query = db.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

    if config.ENVIRONMENT == 'development':
        create_dummy_data()

def create_dummy_data():
    from core.models.division import Division
    from core.models.position import Position
    try:
        for _id, div in config.DIVISIONS.items():
                d = Division(_id)
                db.add(d)
                db.commit()
    except IntegrityError:
        db.rollback()
    try:
        for _id, pos in config.POSITIONS.items():
                p = Position(_id)
                db.add(p)
                db.commit()
    except IntegrityError:
        db.rollback()

    def create_users():
        from core.models.account import User
        users = [
            {
                '_id': '12345',
                'first_name': 'Johnny',
                'last_name': 'Whitworth',
                'email': 'jwhitworth@arizonapipeline.com',
                'profile_pic': 'None',
                'domain': 'arizonapipeline.com',
                'is_active': True
            }
        ]
        for user in users:
            u = User(
                id=user['_id'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                profile_pic=user['profile_pic'],
                domain=user['domain'],
                is_active=user['is_active'],
            )
            db.add(u)
        db.commit()
    create_users()

    def create_profiles():
        from core.models.account import Profile
        profiles = [
            {
                'user_id': '12345',
                'division_id': 1,
                'position_id': 0,
            }
        ]
        for profile in profiles:
            p = Profile(
                user_id=profile['user_id'],
                position_id=profile['position_id'],
                division_id=profile['division_id'],
            )
            db.add(p)
        db.commit()
    create_profiles()

    def create_equipment():
        from core.models.equipment import Equipment
        equipment = [
            {
                'equipment_id': '12345', 
                'description': 'Test Equipment', 
                'serial': 'AB876SD', 
                'model': 'Truck150', 
                'model_year': '2019', 
                'department': 4, 
                'item_class': 11, 
                'job_number': '300000', 
                'warehouse': '32', 
                'division_id': 1,
                'status_code': 1,
            },
            {
                'equipment_id': '12346', 
                'description': 'Test Equipment', 
                'serial': 'AB876SD', 
                'model': 'Truck150', 
                'model_year': '2019', 
                'department': 4, 
                'item_class': 11, 
                'job_number': '300000', 
                'warehouse': '32', 
                'division_id': 1,
                'status_code': 1,
            },
            {
                'equipment_id': '22346', 
                'description': 'Test Equipment', 
                'serial': 'AB876SD', 
                'model': 'Truck150', 
                'model_year': '2019', 
                'department': 4, 
                'item_class': 11, 
                'job_number': '300000', 
                'warehouse': '32', 
                'division_id': 1,
                'status_code': 1,
            },
        ]
        for equip in equipment:
            e = Equipment(
                    equipment_id=equip['equipment_id'], 
                    description=equip['description'], 
                    serial=equip['serial'], 
                    model=equip['model'], 
                    model_year=equip['model_year'], 
                    department=equip['department'], 
                    item_class=equip['item_class'], 
                    job_number=equip['job_number'], 
                    warehouse=equip['warehouse'], 
                    division_id=equip['division_id'],
                    status_code=equip['status_code'],
                    )
            db.add(e)
        db.commit()
    create_equipment()
