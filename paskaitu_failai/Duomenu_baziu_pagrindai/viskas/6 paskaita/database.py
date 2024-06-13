from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('C:\code\paskaitu_failai\Duomenu_baziu_pagrindai\pask6_uzd\database\database.db')


Base = declarative_base()

_sessionMaker = sessionmaker(bind = engine)

def get_db():
    session = _sessionMaker()
    return session
