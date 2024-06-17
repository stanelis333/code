from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def home():
#     return """
#     <h1 style="background-color: lightgreen">Helooo!</h1>
#     """

#http://127.0.0.1:5000/index
@app.route("/")
def index():
    return render_template("index.html")

#http://127.0.0.1:5000/vardai
@app.route("/vardai")
def vardai():
    vardai = ['Tomas', 'Nerius', 'Adamas']
    return render_template("vardai.html", sarasas = vardai)

#http://127.0.0.1:5000/login
@app. route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        input = request.form["vardas"]
        return render_template("pasisveikinimas.html", vardas = input)
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run()
