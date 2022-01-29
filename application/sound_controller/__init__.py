from flask import Blueprint

bp = Blueprint('sound_controller', __name__)

from application.sound_controller import routes