from flask import Flask, render_template, request, redirect, url_for
from database import app
from crud import *

@app.route("/vartotojai")
def vartotojai():
    vartotojai = gauti_visus_vartotojus()
    masinos = gauti_visas_masinas()
    return render_template("vartotojai/index.html", sarasas=vartotojai, sarasas1=masinos)

@app.route("/vartotojai/create", methods=["GET", "POST"])
def vartotojai_create():
    if request.method == "POST":
        name = request.form["vardas"]
        sukurti_vartotoja(name)
        return redirect(url_for("vartotojai"))
    return render_template("vartotojai/create.html")

@app.route("/vartotojai/delete/<int:id>", methods=["GET", "POST"])
def vartotojai_delete(id):
    vartotojas = gauti_vartotoja(id)
    if request.method == "POST":
        istrinti_vartotoja(id)
        return redirect(url_for("vartotojai"))
    return render_template("vartotojai/delete.html", vartotojas=vartotojas)

@app.route("/vartotojai/update/<int:id>", methods=["GET", "POST"])
def vartotojai_update(id):
    vartotojas = gauti_vartotoja(id)
    if request.method == "POST":
        name = request.form["vardas"]
        atnaujinti_vartotoja(id, name)
        return redirect(url_for("vartotojai"))
    return render_template("vartotojai/update.html", vartotojas=vartotojas)

#--------------------------------------------------------------------------------MAŠINOS

@app.route("/masinos/create", methods=["GET", "POST"])
def masinos_create():
    if request.method == "POST":
        brand = request.form["brand"]
        model = request.form["model"]
        year = request.form["year"]
        sukurti_masina(brand, model, year)
        return redirect(url_for("vartotojai"))
    return render_template("masinos/create.html")

@app.route("/masinos/update/<int:id>", methods=["GET", "POST"])
def masinos_update(id):
    masina = gauti_masina(id)
    if request.method == "POST":
        vartotojas_id = request.form["vartotojas_id"]
        if priskirti_masina_vartotojui(id, vartotojas_id):
            return redirect(url_for("vartotojai"))
    return render_template("masinos/update.html", masina=masina)

@app.route("/masinos/delete/<int:id>", methods=["GET", "POST"])
def masinos_delete(id):
    masina = gauti_masina(id)
    if request.method == "POST":
        istrinti_masina(id)
        return redirect(url_for("vartotojai"))
    return render_template("masinos/delete.html", masina=masina)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
