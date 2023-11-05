from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Shhhhh, stay quiet!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    datos = request.form
    name = datos["name"]
    dojo = datos["dojo"]
    language = datos["language"]
    comments = datos["comments"]
    session["datos"] = datos
    return redirect("/result")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/home", methods=["POST"])
def home():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)