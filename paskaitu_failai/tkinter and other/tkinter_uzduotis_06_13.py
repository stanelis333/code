
from tkinter import *

main_window = Tk(className="My Application")
main_window.geometry("300x80")

def pasisveikinti(event=None):
    name = e1.get()
    pasisveikinimas.config(text=f"Sveiki, {name}")
def isvalyti(event=None):
    pasisveikinimas.config(text='')

Label(main_window, text='Įveskite vardą').grid(row=0)
e1 = Entry(main_window)
e1.grid(row=0, column=1)

patvirtinimas = Button(main_window, text='Patvirtinti', command=pasisveikinti).grid(row=0, column=2)
main_window.bind("<Return>", pasisveikinti)
pasisveikinimas = Label(main_window, text='')
pasisveikinimas.grid(row=1, column=1)

meniu = Menu(main_window)
main_window.config(menu=meniu)
sub_menu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=sub_menu)
sub_menu.add_command(label="Išvalyti", command= isvalyti)
sub_menu.add_command(label="Atkurti paskutinį", command=pasisveikinti)
sub_menu.add_separator()
sub_menu.add_command(label="Išeiti", command= exit)
main_window.mainloop()
