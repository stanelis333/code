from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Invoice(Base):
    __tablename__ = "Invoices"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('Users.id'))  # one to many, one User has many Invoices

    user = relationship("User", back_populates="invoices")  # one to many, one User has many Invoices


    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"