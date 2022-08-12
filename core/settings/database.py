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
    {'equipment_id': '14730', 'description': 'TOYOTA', 'model_year': 2018, 'job_number': '300000', 'model': 'TACOMA', 'serial': '5TFNX4CN5EX032652', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 105, 'warehouse': 'DNE'},
    {'equipment_id': '14740', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA9DZ342183', 'status_code': 5, 'division_id': 5,'department': 42,'item_class': 120, 'warehouse': 'DNE'},
    {'equipment_id': '14750', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEAXDZ340720', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 120, 'warehouse': 'DNE'},
    {'equipment_id': '47760', 'description': 'DITCH', 'model_year': 2018, 'job_number': '300000',  'model': 'WITCH', 'serial': '1DSV183T3B1702720', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 432, 'warehouse': 'DNE'},
    {'equipment_id': '13180', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': '3500', 'serial': '1GAHG35U461101050', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '13990', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'EXPEDITION', 'serial': '1FMFU17575LA29180', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '14270', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'EDGE', 'serial': '2FMDK3JC4ABA18938', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '14680', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'ESCAPE', 'serial': '1FMCU0GX3DUB64440', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '11980', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V0XE851432', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '11990', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V2XE850329', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12060', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE851474', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12080', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V1XE851567', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12110', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V0XE850331', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12130', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V7XE851542', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12140', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE851569', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12180', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE850311', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12190', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V6XE850320', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12240', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE851555', 'status_code': 2, 'division_id': 2,'department': 52,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12290', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5YE900206', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12300', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V4YE900214', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12350', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V3YE900222', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12380', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5YE900254',  'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '12420', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V6YE900392', 'status_code': 2, 'division_id': 2,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12440', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14V1YE900266', 'status_code': 2, 'division_id': 2,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12450', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V8YE900278', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12460', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V4YE900410', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12490', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V1YE900297', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12500', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5YE900285', 'status_code': 2, 'division_id': 2,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12510', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V8YE900412', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12540', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '2FTZF1768WCA67825', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '12570', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '2500', 'serial':  '1GDHC24U22E140393', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '12580', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial':  '1GTEC14V11E901391', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12590', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF17WXYKB42605', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '12610', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA',  'serial': '1GTGC33R4YF419091', 'status_code': 2, 'division_id': 2,'department': 205,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '12650', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GBGC34R0YF432214', 'status_code': 2, 'division_id': 2,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12660', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14VX2Z900461', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12680', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTHC29U43E209261', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12690', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14X63Z101196', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12700', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14V33E286894', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12730', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V92Z900306', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12760', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC19T24Z334726', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12820', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA',  'serial': '1GTEC14V85Z211782', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12880', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTHK24U56E119762', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12910', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W26KA89853', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12920', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W46FA21885', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12930', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W96KA94144', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '12990', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D66PA90420', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13000', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D06PA29032', 'status_code': 5, 'division_id': 5,'department': 12,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13010', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D66PA32498', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13020', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D36PA79388', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13030', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10DX6PA85169', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13040', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D86PA69035', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13050', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D07PA29754', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13060', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D97PA20230', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13070', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D87PA19988', 'status_code': 5, 'division_id': 5,'department': 12,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13090', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER',  'serial': '1FTYR14D47PA45312', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13100', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D07PA40897', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13110', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W17FA50827', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13130', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W67NA12094', 'status_code': 7, 'division_id': 7,'department': 12,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13140', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W07KB83847', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13150', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W27NA14845', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13210', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCHC24U67E165728', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13220', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W66KC40115', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '13230', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W26KC47627', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14010', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '2GTEC19CX71514484', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14050', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W17KC02602', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14060', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12WX7KC02601', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14070', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12WX7KC18992', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14080', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W07KC00288', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14090', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W27KC32742', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14100', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W47KC24934', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14110', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W07KC32741', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14130', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF122X6NB58917', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '14140', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W37KC19255', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '14170', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12267KC54062', 'status_code': 7, 'division_id': 7,'department': 82,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14190', 'description': 'CHEVY', 'model_year': 2018, 'job_number': '300000',  'model': 'VAN', 'serial': '1GAHG39K981225746', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14200', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12298KD80014', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '14220', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W58FB69935', 'status_code': 5, 'division_id': 5,'department': 12,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14230', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14C49Z900349', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14240', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W69KC79310', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14290', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GCNCPE00BZ133290', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '14320', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX4BZ269399', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14330', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX9BZ265400', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14340', 'description': 'CHEVY', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX3BZ266705', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14350', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPE01BZ306234', 'status_code': 5, 'division_id': 5,'department': 52,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14370', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPE01BZ323468', 'status_code': 5, 'division_id': 5,'department': 42,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14380', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GB0CVCG8BF206622', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14390', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO',  'serial': '1GC0CXCG9BF103328', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 130, 'warehouse': 'DNE'},
    {'equipment_id': '14400', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF122X7KC37927', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14420', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEAXBZ419074', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14430', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA3BZ377847', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14440', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX6BZ364143', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14450', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA5BZ380586', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14470', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX0BZ353431', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14500', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GCNCPEX7BZ161407', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14510', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX9BZ130093', 'status_code': 6, 'division_id': 6,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14540', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA6BZ391404', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14550', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA4BZ449445', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14560', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA0BZ449037', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100, 'warehouse': 'DNE'},
    {'equipment_id': '14570', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': 'GCRCSE07BZ418508', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14590', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA6CZ151030', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14600', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA0CZ149113', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14610', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA2CZ129848', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14630', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEAXCZ123263', 'status_code': 5, 'division_id': 5,'department': 22,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14640', 'description': 'CHEVY', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA5CZ263804', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14650', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA7CZ278465', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14660', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA2CZ266529', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110, 'warehouse': 'DNE'},
    {'equipment_id': '14670', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRW14W67FB76701', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 120, 'warehouse': 'DNE'},
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

equipment = [
    {'equipment_id': '14730', 'description': 'TOYOTA', 'model_year': 2018, 'job_number': '300000', 'model': 'TACOMA', 'serial': '5TFNX4CN5EX032652', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 105},
    {'equipment_id': '14740', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA9DZ342183', 'status_code': 5, 'division_id': 5,'department': 42,'item_class': 120},
    {'equipment_id': '14750', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEAXDZ340720', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 120},
    {'equipment_id': '47760', 'description': 'DITCH', 'model_year': 2018, 'job_number': '300000',  'model': 'WITCH', 'serial': '1DSV183T3B1702720', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 432},
    {'equipment_id': '13180', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': '3500', 'serial': '1GAHG35U461101050', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 100},
    {'equipment_id': '13990', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'EXPEDITION', 'serial': '1FMFU17575LA29180', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 100},
    {'equipment_id': '14270', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'EDGE', 'serial': '2FMDK3JC4ABA18938', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 100},
    {'equipment_id': '14680', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'ESCAPE', 'serial': '1FMCU0GX3DUB64440', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 100},
    {'equipment_id': '11980', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V0XE851432', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '11990', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V2XE850329', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12060', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE851474', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12080', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V1XE851567', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12110', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V0XE850331', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 110},
    {'equipment_id': '12130', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V7XE851542', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '12140', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE851569', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '12180', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE850311', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12190', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V6XE850320', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12240', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5XE851555', 'status_code': 2, 'division_id': 2,'department': 52,'item_class': 110},
    {'equipment_id': '12290', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5YE900206', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12300', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V4YE900214', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12350', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V3YE900222', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12380', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5YE900254',  'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '12420', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V6YE900392', 'status_code': 2, 'division_id': 2,'department': 22,'item_class': 110},
    {'equipment_id': '12440', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14V1YE900266', 'status_code': 2, 'division_id': 2,'department': 22,'item_class': 110},
    {'equipment_id': '12450', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V8YE900278', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12460', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V4YE900410', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12490', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V1YE900297', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12500', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V5YE900285', 'status_code': 2, 'division_id': 2,'department': 2,'item_class': 110},
    {'equipment_id': '12510', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V8YE900412', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 110},
    {'equipment_id': '12540', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '2FTZF1768WCA67825', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '12570', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '2500', 'serial':  '1GDHC24U22E140393', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '12580', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial':  '1GTEC14V11E901391', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12590', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF17WXYKB42605', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '12610', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA',  'serial': '1GTGC33R4YF419091', 'status_code': 2, 'division_id': 2,'department': 205,'item_class': 100},
    {'equipment_id': '12650', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GBGC34R0YF432214', 'status_code': 2, 'division_id': 2,'department': 2,'item_class': 110},
    {'equipment_id': '12660', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14VX2Z900461', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12680', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTHC29U43E209261', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '12690', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14X63Z101196', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12700', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14V33E286894', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12730', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GTEC14V92Z900306', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '12760', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC19T24Z334726', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '12820', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA',  'serial': '1GTEC14V85Z211782', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '12880', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTHK24U56E119762', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12910', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W26KA89853', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12920', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W46FA21885', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12930', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W96KA94144', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '12990', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D66PA90420', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13000', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D06PA29032', 'status_code': 5, 'division_id': 5,'department': 12,'item_class': 110},
    {'equipment_id': '13010', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D66PA32498', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13020', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D36PA79388', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13030', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10DX6PA85169', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '13040', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR10D86PA69035', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '13050', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D07PA29754', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '13060', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D97PA20230', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '13070', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D87PA19988', 'status_code': 5, 'division_id': 5,'department': 12,'item_class': 110},
    {'equipment_id': '13090', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER',  'serial': '1FTYR14D47PA45312', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13100', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'RANGER', 'serial': '1FTYR14D07PA40897', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '13110', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W17FA50827', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13130', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W67NA12094', 'status_code': 7, 'division_id': 7,'department': 12,'item_class': 110},
    {'equipment_id': '13140', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W07KB83847', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13150', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W27NA14845', 'status_code': 7, 'division_id': 7,'department': 32,'item_class': 110},
    {'equipment_id': '13210', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCHC24U67E165728', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13220', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W66KC40115', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '13230', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W26KC47627', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '14010', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '2GTEC19CX71514484', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '14050', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W17KC02602', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '14060', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12WX7KC02601', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '14070', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12WX7KC18992', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14080', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W07KC00288', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14090', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W27KC32742', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14100', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W47KC24934', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14110', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W07KC32741', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14130', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF122X6NB58917', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '14140', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W37KC19255', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '14170', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12267KC54062', 'status_code': 7, 'division_id': 7,'department': 82,'item_class': 110},
    {'equipment_id': '14190', 'description': 'CHEVY', 'model_year': 2018, 'job_number': '300000',  'model': 'VAN', 'serial': '1GAHG39K981225746', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14200', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12298KD80014', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '14220', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRX12W58FB69935', 'status_code': 5, 'division_id': 5,'department': 12,'item_class': 110},
    {'equipment_id': '14230', 'description': 'GMC', 'model_year': 2018, 'job_number': '300000', 'model': 'SIERRA', 'serial': '1GTEC14C49Z900349', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '14240', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF12W69KC79310', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110},
    {'equipment_id': '14290', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GCNCPE00BZ133290', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '14320', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX4BZ269399', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110},
    {'equipment_id': '14330', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX9BZ265400', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110},
    {'equipment_id': '14340', 'description': 'CHEVY', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX3BZ266705', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14350', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPE01BZ306234', 'status_code': 5, 'division_id': 5,'department': 52,'item_class': 110},
    {'equipment_id': '14370', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPE01BZ323468', 'status_code': 5, 'division_id': 5,'department': 42,'item_class': 110},
    {'equipment_id': '14380', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GB0CVCG8BF206622', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110},
    {'equipment_id': '14390', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO',  'serial': '1GC0CXCG9BF103328', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 130},
    {'equipment_id': '14400', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRF122X7KC37927', 'status_code': 2, 'division_id': 2,'department': 32,'item_class': 110},
    {'equipment_id': '14420', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEAXBZ419074', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110},
    {'equipment_id': '14430', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA3BZ377847', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110},
    {'equipment_id': '14440', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX6BZ364143', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110},
    {'equipment_id': '14450', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA5BZ380586', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110},
    {'equipment_id': '14470', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX0BZ353431', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110},
    {'equipment_id': '14500', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': '1500', 'serial': '1GCNCPEX7BZ161407', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110},
    {'equipment_id': '14510', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEX9BZ130093', 'status_code': 6, 'division_id': 6,'department': 22,'item_class': 110},
    {'equipment_id': '14540', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA6BZ391404', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14550', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA4BZ449445', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110},
    {'equipment_id': '14560', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA0BZ449037', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 100},
    {'equipment_id': '14570', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': 'GCRCSE07BZ418508', 'status_code': 7, 'division_id': 7,'department': 22,'item_class': 110},
    {'equipment_id': '14590', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA6CZ151030', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110},
    {'equipment_id': '14600', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA0CZ149113', 'status_code': 2, 'division_id': 2,'department': 110,'item_class': 110},
    {'equipment_id': '14610', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA2CZ129848', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 110},
    {'equipment_id': '14630', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEAXCZ123263', 'status_code': 5, 'division_id': 5,'department': 22,'item_class': 110},
    {'equipment_id': '14640', 'description': 'CHEVY', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA5CZ263804', 'status_code': 5, 'division_id': 5,'department': 32,'item_class': 110},
    {'equipment_id': '14650', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA7CZ278465', 'status_code': 5, 'division_id': 5,'department': 102,'item_class': 110},
    {'equipment_id': '14660', 'description': 'CHEVROLET', 'model_year': 2018, 'job_number': '300000', 'model': 'SILVERADO', 'serial': '1GCNCPEA2CZ266529', 'status_code': 5, 'division_id': 5,'department': 122,'item_class': 110},
    {'equipment_id': '14670', 'description': 'FORD', 'model_year': 2018, 'job_number': '300000', 'model': 'F150', 'serial': '1FTRW14W67FB76701', 'status_code': 7, 'division_id': 7,'department': 2,'item_class': 120},
]