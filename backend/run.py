from app import create_app
from app.extensions import socketio as sio

app = create_app()

if __name__ == "__main__":
    sio.run(app, host="0.0.0.0", port=5000, debug=True)
