from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///paskaitu_failai/Duomenu_baziu_pagrindai/db.failai/Vartotojai_Database.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, age: {self.age}"
    

Base.metadata.create_all(engine)