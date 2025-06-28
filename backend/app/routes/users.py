from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import User, Match
from ..extensions import db
from . import users_bp

# ─────────────── PROFIL JEDNEGO UŻYTKOWNIKA ────────────────
@users_bp.get("/<int:user_id>")
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(
        id=user.id,
        name=user.name,
        age=user.age,
        image=user.image,
        description=user.description,
    )

# ─────────────── LISTA KANDYDATÓW DO SWIPE ────────────────
@users_bp.get("/recommendations")
@jwt_required()
def recommendations():
    me = get_jwt_identity()
    # znajdź ID-ki osób, które już oceniliśmy (like/skip)
    rated = db.session.execute(
        """
        SELECT user2_id FROM matches WHERE user1_id = :me
        UNION
        SELECT user1_id FROM matches WHERE user2_id = :me
        """,
        {"me": me},
    ).scalars()
    users = (
        User.query.filter(User.id.not_in(rated), User.id != me)
        .limit(20)  # proste stronicowanie
        .all()
    )
    return jsonify(
        [
            {
                "id": u.id,
                "name": u.name,
                "age": u.age,
                "image": u.image,
                "description": u.description,
            }
            for u in users
        ]
    )
