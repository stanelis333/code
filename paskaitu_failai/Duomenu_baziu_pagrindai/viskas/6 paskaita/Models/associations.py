from sqlalchemy import Column, Integer, Table, ForeignKey
from database import Base

# many to many Roles with Users
role_user_associasion = Table(
    "role_user", # table name
    Base.metadata, # Base inheritange
    Column('user_id', Integer, ForeignKey('Users.id')),
    Column('role_id', Integer, ForeignKey('Roles.id'))
)