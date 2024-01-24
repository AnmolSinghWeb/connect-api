# import os
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy import create_engine
# import chromadb
# from chromadb.config import Settings

# Base = declarative_base()
# _SESSION_FACTORY = None

# # client = chroma_client = chromadb.HttpClient(host='localhost', port=8000, settings=Settings(allow_reset=True, anonymized_telemetry=False))

# if 'DATABASE_URL' in os.environ:
#     engine = create_engine(os.environ['DATABASE_URL'], pool_size=20, max_overflow=-1, \
#             pool_recycle=180, pool_use_lifo=True, \
#                 connect_args={"options": "-c statement_timeout=50000"})
#     _SESSION_FACTORY = sessionmaker(bind=engine)

# def session_factory() -> Session:
#     return _SESSION_FACTORY()
