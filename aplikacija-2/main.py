from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/onama")
def onama():
    return render_template("onama.html")

@app.route("/usluge")
def usluge():
    return render_template("usluge.html")


if __name__ == "__main__":
    app.run()