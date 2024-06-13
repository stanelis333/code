from database import get_db
from Models.employees import Employee
from Models.projects import Project
from Models.departaments import Department


session = get_db()

#------employee CRUD-------------------------------------

def create_employ(name, last_name, birt_date, position, salary):
    employ = Employee(name, last_name, birt_date, position, salary)

    session.add(employ)
    session.commit()

def get_all_employ():
    employ = session.query(Employee).all()
    return employ

#------project CRUD-------------------------------------

def create_proj(name):
    proj = Project(name)
    session.add(proj)
    session.commit()

def get_all_proj():
    proj = session.query(Project).all()
    return proj

#------department CRUD-------------------------------------


def create_dep(name):
    dep = Department(name)
    session.add(dep)
    session.commit()


def add_empl_to_dep(empl_id, dep_id):
    emplo = session.get(Employee, empl_id)
    dep = session.get(Department, dep_id)

    if emplo and dep:
        emplo.department = dep
        session.commit()
        print("Commit successful")
    else:
        if not emplo:
            print(f"Employee with ID {empl_id} not found")
        if not dep:
            print(f"Department with ID {dep_id} not found")


#------Relationship - Association-------------------------------------

def add_empl_to_proj(empl_id, proj_id):
    emplo = session.get(Employee, empl_id)
    proje = session.get(Project, proj_id)

    if emplo and proje:
        emplo.proj.append(proje)
        session.commit()

def get_empl_proj(empl_id):
    empl = session.get(Employee, empl_id)
    return empl.proj
