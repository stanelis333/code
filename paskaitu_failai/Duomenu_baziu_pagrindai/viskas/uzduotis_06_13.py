
from tkinter import *

main_window = Tk(className="My Application")
main_window.geometry("300x80")

def pasisveikinti():
    name = e1.get()
    pasisveikinimas.config(text=f"Sveiki, {name}")

Label(main_window, text='Įveskite vardą').grid(row=0)
e1 = Entry(main_window)
e1.grid(row=0, column=1)

Button(main_window, text='Patvirtinti', command=pasisveikinti).grid(row=0, column=2)
pasisveikinimas = Label(main_window, text='')
pasisveikinimas.grid(row=1, column=1)
main_window.mainloop()



