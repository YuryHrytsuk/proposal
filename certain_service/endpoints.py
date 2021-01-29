from flask import Blueprint

app_bp = Blueprint('app', __name__)


@app_bp.route("/")
def hello_world():
    return "Hello, World!"
