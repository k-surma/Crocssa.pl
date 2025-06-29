from flask import Flask, send_from_directory
from flask_cors import CORS
from models import db
from config import Config
from auth.routes import auth_bp

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='')
app.config.from_object(Config)
CORS(app)

db.init_app(app)
app.register_blueprint(auth_bp)


# Serve SPA
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)