import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

Base = declarative_base()
_SESSION_FACTORY = None

if 'DATABASE_URL' in os.environ:
    engine = create_engine(os.environ['DATABASE_URL'], pool_size=20, max_overflow=-1, \
            pool_recycle=180, pool_use_lifo=True, \
                connect_args={"options": "-c statement_timeout=50000"})
    _SESSION_FACTORY = sessionmaker(bind=engine)

def session_factory() -> Session:
    return _SESSION_FACTORY()
