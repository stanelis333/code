
from tkinter import *

# from tkinter import *
# root = Tk()
# w = Label(root, text=(
#     '''
#     DARBUOTOJŲ VALDYMO PROGRAMA

#     1. Parodyti visus darbuotojus
#     2. Pridėti naują darbuotoja
#     3. Surasti darbuotoja pagal id
#     4. Pakeisti darbuotojo duomenis
#     5. Pašalinti darbuotoja
#     6. Uždaryti programą

#     Pasirinkite: '''
#     ))
# w.pack()
# root.mainloop()



# import tkinter as tk
# r = tk.Tk()
# r.title('DARBUOTOJŲ VALDYMO PROGRAMA')

# button = tk.Button(r, text='Parodyti visus darbuotojus', width=55, command=r.destroy)
# button2 = tk.Button(r, text='Pridėti naują darbuotoja', width=55, command=r.destroy)
# button3 = tk.Button(r, text='Surasti darbuotoja pagal id', width=55, command=r.destroy)
# button4 = tk.Button(r, text='Pakeisti darbuotojo duomenis', width=55, command=r.destroy)
# button5 = tk.Button(r, text='Pašalinti darbuotoja', width=55, command=r.destroy)
# button6 = tk.Button(r, text='Uždaryti programą', width=55, command=r.destroy)
# button.pack()
# button2.pack()
# button3.pack()
# button4.pack()
# button5.pack()
# button6.pack()
# r.mainloop()

# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()


# from tkinter import *

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# mylist = Listbox(root, yscrollcommand=scrollbar.set)

# for line in range(100):
#     mylist.insert(END, str(line))
    
# mylist.pack(side=LEFT, fill=BOTH)
# scrollbar.config(command=mylist.yview)
# mainloop()





# master = Tk(screenName=None,  baseName=None,  className='Darbuotojai',  useTk=1)
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()


# import tkinter as tk

# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()












#####################
# from uzduotys_5 import Employees
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from tkinter import *
# import tkinter as tk

# # Setting up the database connection
# engine = create_engine('sqlite:///paskaitu_failai/Duomenu_baziu_pagrindai/db.failai/Darbuotojai_2uzd.db')
# SessionMaker = sessionmaker(bind=engine)
# session = SessionMaker()

# # Functions to be called by buttons
# def show_all_employees():
#     employees = session.query(Employees).all()
#     for employee in employees:
#         print(employee)

# def add_employee():
#     name = input("Įveskite darbuotojo vardą: ")
#     last_name = input("Įveskite darbuotojo pavardę: ")
#     birth_date = input("Įveskite darbuotojo gimimo metus: ")
#     position = input("Įveskite darbuotojo pareigas: ")
#     salary = input("Įveskite darbuotojo atlyginimą: ")
#     employee = Employees(name, last_name, birth_date, position, salary)
#     session.add(employee)
#     session.commit()

# def find_employee_by_id():
#     id = int(input("Įveskite darbuotojo id: "))
#     employee = session.get(Employees, id)
#     print(employee)

# def update_employee_data():
#     id = int(input("Įveskite darbuotojo id: "))
#     pasirinkimas_keisti = input('\nKą norėtumėte keisti?\n1. Vardą\n2. Pavardę\n3. Gimimo metus\n4. Pareigas\n5. Atlyginimą \n\nĮveskite:')        
#     employee = session.get(Employees, id)

#     if pasirinkimas_keisti == "1":
#         new_name = input("Įveskite naują darbuotojo vardą: ")
#         employee.name = new_name
#     elif pasirinkimas_keisti == "2":
#         new_last_name = input("Įveskite naują darbuotojo pavardę: ")
#         employee.last_name = new_last_name
#     elif pasirinkimas_keisti == "3":
#         new_bday = input("Įveskite naują darbuotojo gimimo datą: ")
#         employee.birth_date = new_bday
#     elif pasirinkimas_keisti == "4":
#         new_position = input("Įveskite naujas darbuotojo pareigas: ")
#         employee.position = new_position
#     elif pasirinkimas_keisti == "5":
#         new_salary = input("Įveskite naują darbuotojo atlyginimą: ")
#         employee.salary = new_salary

#     session.commit()

# def delete_employee():
#     id = int(input("Įveskite šalinamo darbuotojo id: "))
#     employee = session.get(Employees, id)
#     session.delete(employee)
#     session.commit()

# def close_program():
#     print("Išeinama iš programos..")
#     r.destroy()

# # Setting up the Tkinter window
# r = tk.Tk()
# r.title('DARBUOTOJŲ VALDYMO PROGRAMA')

# button = tk.Button(r, text='Parodyti visus darbuotojus', width=55, command=show_all_employees)
# button2 = tk.Button(r, text='Pridėti naują darbuotoja', width=55, command=add_employee)
# button3 = tk.Button(r, text='Surasti darbuotoja pagal id', width=55, command=find_employee_by_id)
# button4 = tk.Button(r, text='Pakeisti darbuotojo duomenis', width=55, command=update_employee_data)
# button5 = tk.Button(r, text='Pašalinti darbuotoja', width=55, command=delete_employee)
# button6 = tk.Button(r, text='Uždaryti programą', width=55, command=close_program)

# button.pack()
# button2.pack()
# button3.pack()
# button4.pack()
# button5.pack()
# button6.pack()

# r.mainloop()



# #####################