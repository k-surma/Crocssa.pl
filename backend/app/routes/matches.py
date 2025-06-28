from datetime import datetime
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Match, User
from ..extensions import db
from . import matches_bp

# ─────────────── SWIPE (like/skip) ────────────────
@matches_bp.post("/<int:target_id>")
@jwt_required()
def like_user(target_id):
    me = get_jwt_identity()
    # Sprawdź czy już istniało odwrotne polubienie
    existing = Match.query.filter_by(user1_id=target_id, user2_id=me).first()
    if existing:
        # „Super! Mamy match”
        existing.matched_at = datetime.utcnow()  # odśwież datę
        db.session.commit()
        return jsonify(match=True, match_id=existing.id)

    # Dodaj jednostronny like (me -> target)
    new_like = Match(user1_id=me, user2_id=target_id, matched_at=None)
    db.session.add(new_like)
    db.session.commit()
    return jsonify(match=False)

# ─────────────── LISTA MOICH MATCHY ────────────────
@matches_bp.get("/")
@jwt_required()
def my_matches():
    me = get_jwt_identity()
    matches = Match.query.filter(
        ((Match.user1_id == me) | (Match.user2_id == me)) & (Match.matched_at != None)  # noqa: E711
    ).all()
    def _other(m):  # wyciągnij „drugą stronę”
        return m.user2_id if m.user1_id == me else m.user1_id

    return jsonify(
        [
            {
                "match_id": m.id,
                "user": User.query.get(_other(m)).name,
                "user_id": _other(m),
                "matched_at": m.matched_at.isoformat(),
            }
            for m in matches
        ]
    )
