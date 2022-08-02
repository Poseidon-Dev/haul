from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite://///Users/mr.biscuits/Dev/haul/sqlite.db')
db = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
