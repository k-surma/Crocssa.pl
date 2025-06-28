from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Message
from ..extensions import db
from . import messages_bp

# ─────────────── HISTORIA CZATU ────────────────
@messages_bp.get("/<int:match_id>")
@jwt_required()
def history(match_id):
    msgs = (
        Message.query.filter_by(match_id=match_id)
        .order_by(Message.timestamp.asc())
        .all()
    )
    return jsonify(
        [
            {
                "id": m.id,
                "sender_id": m.sender_id,
                "body": m.message,
                "timestamp": m.timestamp.isoformat(timespec="seconds"),
            }
            for m in msgs
        ]
    )

# ─────────────── WYSYŁANIE WIADOMOŚCI ────────────────
@messages_bp.post("/<int:match_id>")
@jwt_required()
def send_msg(match_id):
    me = get_jwt_identity()
    body = request.json["body"]
    msg = Message(
        sender_id=me,
        receiver_id=request.json["receiver_id"],
        match_id=match_id,
        message=body,
    )
    db.session.add(msg)
    db.session.commit()
    return jsonify(id=msg.id, timestamp=msg.timestamp.isoformat(timespec="seconds"))
