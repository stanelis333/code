import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base 

engine = create_engine('sqlite:///paskaitu_failai/Duomenu_baziu_pagrindai/db.failai/Darbuotojai_2uzd.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = "Darbuotojai"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    birth_date = Column(String)
    position = Column(String)
    salary = Column(Integer)
    work_from = Column(DateTime, default = datetime.datetime.now)

    def __init__ (self, name, last_name, birth_date, position, salary):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.position = position
        self.salary = salary
        
    def __repr__(self):
        return f"ID: {self.id} | Vardas: {self.name} | Pavardė: {self.last_name} | Gimimo Metai: {self.birth_date} | Pareigos: {self.position} | Atlyginimas: {self.salary} | Dirba nuo: {self.work_from.strftime('%Y-%m-%d')}"
    

Base.metadata.create_all(engine)