from flask import Flask, render_template, request
from database import app
from crud import *

# #http://127.0.0.1:5000
# @app.route("/")
# def home():
#     print("hey")    
#     return """
#     <div style="background-color: grey">
#         <h1>Labas, pasauli!</h1>
#         <p>This is a paragraph.</p>
#     </div>
#     """

#http://127.0.0.1:5000/vartotojai
@app.route("/vartotojai")
def vartotojai():
    vartotojai = gauti_visus_vartotojus()
    return render_template("vartotojai/index.html", sarasas = vartotojai)


#http://127.0.0.1:5000/vartotojai/Create
@app.route("/vartotojai/create", methods = ["GET", "POST"])
def vartotojai_create():
    if request.method == "POST":
        name = request.form["vardas"]
        age = request.form["amzius"]
        sukurti_vartotoja(name, age)
        return render_template("vartotojai/message.html", message = f"Sėkmingai sukurtas vartotojas - {name}")
    else:
        return render_template("vartotojai/create.html")
    
#http://127.0.0.1:5000/vartotojai/delete/<id>
@app.route("/vartotojai/delete/<id>", methods = ["GET", "POST"])
def vartotojai_delete(id):
    vartotojas = gauti_vartotoja(id)
    if vartotojas is None:
        return render_template("vartotojai/message.html", message = f"Nėra vartotojo su id - {id}")
    
    if request.method == "POST":
        istrinti_vartotoja(id)
        return render_template("vartotojai/message.html", message = f"Sėkmingai ištrintas vartotojas - {vartotojas.name}")
    else:
        return render_template("vartotojai/delete.html",  vartotojas = vartotojas)

#http://127.0.0.1:5000/vartotojai/update/<id>
@app.route("/vartotojai/update/<id>", methods = ["GET", "POST"])
def vartotojai_update(id):
    vartotojas = gauti_vartotoja(id)
    if vartotojas is None:
        return render_template("vartotojai/message.html", message = f"Nėra vartotojo su id - {id}")
    
    if request.method == "POST":
        name = request.form["vardas"]
        age = request.form["amzius"]
        atnaujinti_vartotoja(id, name, age)
        return render_template("vartotojai/message.html", message = f"Sėkmingai atnaujintas vartotojas - {vartotojas.name}")
    else:
        return render_template("vartotojai/update.html",  vartotojas = vartotojas) 


# #http://127.0.0.1:5000/vartotojai/<id>
# @app.route("/vartotojai/<id>")
# def print_name(id):
#     #kraunu iš DB
#     return f"Labas, vartotojo id yra {id}"

#http://127.0.0.1:5000/index
@app.route("/")
def index():
    return render_template("index.html")

#http://127.0.0.1:5000/vardai
@app.route("/vardai")
def vardai():
    vardai = ["Rokas", "Tomas", "Paulius", "Diana", "Mantas"]
    return render_template("vardai.html", sarasas = vardai)

#http://127.0.0.1:5000/login
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("pasisveikinimas.html", vardas = vardas)
    else:
        return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
