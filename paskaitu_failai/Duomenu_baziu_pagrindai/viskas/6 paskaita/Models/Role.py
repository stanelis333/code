from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from Models.associations import role_user_associasion


class Role(Base):
    __tablename__ = "Roles"

    id = Column(Integer, primary_key = True)
    name = Column(String)

    users = relationship("User", secondary= role_user_associasion, back_populates="roles")# many to many Roles with Users


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"

