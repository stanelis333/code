from database import get_db
from Models.User import User
from Models.Role import Role
from Models.Invoice import Invoice

session = get_db()

#------User CRUD-------------------------------------

def create_user(name, age):
    user = User(name, age)

    session.add(user)
    session.commit()

def get_all_users():
    users = session.query(User).all()
    return users

#------Roles CRUD-------------------------------------

def create_role(name):
    role = Role(name)

    session.add(role)
    session.commit()

def get_all_roles():
    roles = session.query(Role).all()
    return roles

#------Invoices CRUD-------------------------------------

def create_invoice(name, invoice_for_user_id):
    invoice = Invoice(name, invoice_for_user_id)

    session.add(invoice)
    session.commit()

def get_all_invoices_by_user_id(user_id):
    user = session.get(User, user_id)
    return user.invoices

#------Relationship - Association-------------------------------------

def add_role_to_user(user_id, role_id):
    user = session.get(User, user_id)# gets the user by id
    role = session.get(Role, role_id)# gets the role by id

    if user and role: # check if not None
        user.roles.append(role)# we append role to user roles list
        session.commit()

def get_user_roles(user_id):
    user = session.get(User, user_id)
    return user.roles
