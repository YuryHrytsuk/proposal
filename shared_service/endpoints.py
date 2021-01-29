import flask
from flask.blueprints import Blueprint


shared_bp = Blueprint("shared", __name__)


@shared_bp.route("/stats")
def stats_endpoint():
    return flask.jsonify({"stat_1": "value 1", "stat_2": "value 2"})
