from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from database import Base
from Models.associations import role_user_associasion
from Models.Invoice import Invoice



class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.now)

    roles = relationship("Role", secondary=role_user_associasion, back_populates="users") # many to many Roles with Users
    invoices = relationship("Invoice", back_populates="user") # one to many, one User has many Invoices


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, age: {self.age} {self.created_date.date()}"

