from flask import Flask
from config import Config
from flask_bootstrap  import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

from application.sound_controller import bp as sound_controller_bp
app.register_blueprint(sound_controller_bp)

from application.main import bp as main_bp
app.register_blueprint(main_bp)

from application.memes import bp as memes_bp
app.register_blueprint(memes_bp)

from application.twitch_streams import bp as twitch_streams_bp
app.register_blueprint(twitch_streams_bp)