from flask import Blueprint

bp = Blueprint('memes', __name__)

from application.memes import routes