import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .associations import emplo_proj_associasion
from database import Base

class Employee(Base):
    __tablename__ = "Employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    birth_date = Column(String)
    position = Column(String)
    salary = Column(Integer)
    work_from = Column(DateTime, default = datetime.datetime.now)
    department_id = Column(Integer, ForeignKey("Departments.id"))
    project_id = Column(Integer, ForeignKey('Projects.id'))
    proj = relationship("Project", secondary=emplo_proj_associasion, back_populates="emplo")
    department = relationship("Department", back_populates="employees")

    def __init__ (self, name, last_name, birth_date, position, salary):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.position = position
        self.salary = salary
        
    def __repr__(self):
        return f"ID: {self.id} | Vardas: {self.name} | Pavardė: {self.last_name} | Gimimo Metai: {self.birth_date} | Pareigos: {self.position} | Atlyginimas: {self.salary} | Dirba nuo: {self.work_from.strftime('%Y-%m-%d')}"
    

