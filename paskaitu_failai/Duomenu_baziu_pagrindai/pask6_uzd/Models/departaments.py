from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from database import Base

class Department(Base):
    __tablename__ = "Departments"

    id = Column(Integer, primary_key=True)
    name = Column(String)   
    
    employees = relationship("Employee", back_populates="department")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Department name: {self.name}"