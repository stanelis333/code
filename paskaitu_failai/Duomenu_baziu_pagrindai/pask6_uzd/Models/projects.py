
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from .associations import emplo_proj_associasion
from database import Base

class Project(Base):
    __tablename__ = "Projects"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    test = Column(String)
    tes2 = Column(String)

    emplo = relationship("Employee", secondary=emplo_proj_associasion, back_populates="proj")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Projekto pavadinimas: {self.name}"