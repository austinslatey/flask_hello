from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))

if __name__  == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)