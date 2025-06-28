from flask import Flask
from .config import Config
from .extensions import db, jwt, cors, socketio as sio   # 👈 alias
from .routes import auth_bp, users_bp, matches_bp, messages_bp
from .socketio.events import register_socketio_events

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})
    sio.init_app(app)             # 👈 używamy aliasu

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(matches_bp)
    app.register_blueprint(messages_bp)

    register_socketio_events(sio)
    return app
