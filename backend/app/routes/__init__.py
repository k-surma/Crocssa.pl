from flask import Blueprint
auth_bp    = Blueprint("auth",    __name__, url_prefix="/api/auth")
users_bp   = Blueprint("users",   __name__, url_prefix="/api/users")
matches_bp = Blueprint("matches", __name__, url_prefix="/api/matches")
messages_bp= Blueprint("messages",__name__, url_prefix="/api/messages")

from . import auth, users, matches, messages  # noqa
