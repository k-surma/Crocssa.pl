"""
Ładny, jednopunktowy eksport zdarzeń Socket.IO.
Importujemy tutaj funkcję register_socketio_events,
żeby `from app.socketio import register_socketio_events`
działało zarówno w run.py, jak i w testach.
"""

from .events import register_socketio_events  # noqa: F401
