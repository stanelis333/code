from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///C:/code/paskaitu_failai/Duomenu_baziu_pagrindai/pask6_uzd/database1/database.db')
Base = declarative_base()

SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

def get_db():
    session = SessionMaker()
    return session
