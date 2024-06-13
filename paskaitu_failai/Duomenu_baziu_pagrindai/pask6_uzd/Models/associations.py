from sqlalchemy import Column, Integer, Table, ForeignKey
from database import Base

# many to many Roles with Users
emplo_proj_associasion = Table(
    "emplo_proj", 
    Base.metadata, 
    Column('employee_id', Integer, ForeignKey('Employees.id')),
    Column('project_id', Integer, ForeignKey('Projects.id'))
)



# emplo_dep_associations = Table(
#     "emplo_dep",
#     Base.metadata,
#     Column('employee_id', Integer, ForeignKey('Employees.id')),
#     Column('department_id', Integer, ForeignKey('Departments.id'))
# )