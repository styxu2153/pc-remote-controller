from flask import Blueprint

bp = Blueprint('twitch_streams', __name__)

from application.twitch_streams import routes