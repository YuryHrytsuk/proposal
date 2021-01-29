from flask import Flask

from certain_service.endpoints import app_bp  # instead of `from endpoints import app_bp`
from shared_service.endpoints import shared_bp  # instead of `from endpoints import shared_bp`


def create_app():
    app_ = Flask(__name__)

    app_.register_blueprint(app_bp)
    app_.register_blueprint(shared_bp)

    return app_


if __name__ == "__main__":
    app = create_app()
    app.run(host="localhost", port=8000)
