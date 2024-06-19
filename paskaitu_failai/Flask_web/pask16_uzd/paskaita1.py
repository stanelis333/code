from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/<word>')
def repeat_word(word):
    repeated_word = [(word + ' ') * 5]
    return render_template("zodziai.html", sarasas = repeated_word)

@app. route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        input = request.form["vardas"]
        return render_template("x5.html", vardas = input)
    else:
        return render_template("login.html")
    
@app. route("/ar_keliamieji", methods = ["GET", "POST"])
def keliamieji():
    if request.method == "POST":
        input_metai = int(request.form["metai"])
        return render_template("tikrinti_metus.html", metai=input_metai)
    else:
        return render_template("ar_keliamieji.html")

def keliamieji(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

@app.route('/keliamieji')
def show_leap_years():
    leap_years = [year for year in range(1900, 2101) if keliamieji(year)]
    return render_template("visi_keliamieji.html", sarasas = leap_years)

if __name__ == "__main__":
    app.run()
