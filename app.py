from flask import flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "CI/CD с GitHub Actions + Minikube работает!"

