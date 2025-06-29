import os
from flask import Flask
from .config import Config
from .extensions import db, jwt, cors, socketio as sio   # 👈 alias
from .routes import auth_bp, users_bp, matches_bp, messages_bp
from .socketio.events import register_socketio_events
from .routes.upload import upload_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config["UPLOAD_FOLDER"] = "/app/uploads"
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})
    sio.init_app(app)             # 👈 używamy aliasu

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(matches_bp)
    app.register_blueprint(messages_bp)
    app.register_blueprint(upload_bp)

    register_socketio_events(sio)
    return app
