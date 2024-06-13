from uzduotys_5 import Employees
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tkinter import *
import tkinter as tk

engine = create_engine('sqlite:///paskaitu_failai/Duomenu_baziu_pagrindai/db.failai/Darbuotojai_2uzd.db')
SessionMaker = sessionmaker(bind= engine)
session = SessionMaker()


def show_all():
    employees = session.query(Employees).all()
    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    mylist = Listbox(root, yscrollcommand=scrollbar.set, width=115)
    for employee in employees:
        mylist.insert(END, str(employee))       
    mylist.pack(side=LEFT, fill=BOTH, )
    scrollbar.config(command=mylist.yview)
    mainloop()

def add_emp():
    master = Tk()
    Label(master, text='Įveskite darbuotojo vardą').grid(row=0)
    Label(master, text='Įveskite darbuotojo pavarde').grid(row=1)
    Label(master, text='Įveskite darbuotojo gimimo metus').grid(row=2)
    Label(master, text='Įveskite darbuotojo pareigas').grid(row=3)
    Label(master, text='Įveskite darbuotojo atlyginima').grid(row=4)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)

    def save_employee():
        name = e1.get()
        last_name = e2.get()
        birth_date = e3.get()
        position = e4.get()
        salary = e5.get()
        
        employee = Employees(name, last_name, birth_date, position, salary)
        session.add(employee)
        session.commit()
        master.destroy()
    Button(master, text='Išsaugoti', command=save_employee).grid(row=5, column=0, columnspan=2)
    
    
def find_emp():
    master = Tk()
    Label(master, text='Įveskite darbuotojo id: ').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
       
    def find():
        ee = e1.get()
        employee = session.get(Employees, ee)
        Label(master, text=f"{employee}").grid(row=1)

    Button(master, text='Ieškoti', command=find).grid(row=3, column=0, columnspan=2)

def change_data():
    id = int(input("Įveskite vartotojo id: "))
    pasirinkimas_keisti = input('\nKą norėtumėte keisti?\n1. Vardą\n2. Pavardę\n3. Gimimo metus\n4. Pareigas\n5. Atlyginimą \n\nĮveskite:')        
    employee = session.get(Employees, id)

    if pasirinkimas_keisti == "1":
        new_name = input("Įveskite naują darbuotojo vardą: ")           
        employee.name = new_name

    if pasirinkimas_keisti == "2":
        new_last_name = input("Įveskite naują vartotojo Pavardę: ")
        employee.last_name = new_last_name

    if pasirinkimas_keisti == "3":
        new_bday = input("Įveskite naują darbuotojo gimimo data: ")
        employee.birth_date = new_bday

    if pasirinkimas_keisti == "4":
        new_position = input("Įveskite naujas dabuotojo pareigas: ")
        employee.position = new_position

    if pasirinkimas_keisti == "5":
        new_salary = input("Įveskite naują darbuotojo atlyginima: ")
        employee.salary = new_salary

def delete():
    id = int(input("Įveskite šalinamo darbuotojo id: "))
    employee = session.get(Employees, id)
    session.delete(employee)
    session.commit ()



r = tk.Tk()
r.title('DARBUOTOJŲ VALDYMO PROGRAMA')

button = tk.Button(r, text='Parodyti visus darbuotojus', width=55, command=show_all)
button2 = tk.Button(r, text='Pridėti naują darbuotoja', width=55, command=add_emp)
button3 = tk.Button(r, text='Surasti darbuotoja pagal id', width=55, command=find_emp)
button4 = tk.Button(r, text='Pakeisti darbuotojo duomenis', width=55, command=change_data)
button5 = tk.Button(r, text='Pašalinti darbuotoja', width=55, command=delete)
button6 = tk.Button(r, text='Uždaryti programą', width=55, command=r.destroy)
button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
r.mainloop()





    