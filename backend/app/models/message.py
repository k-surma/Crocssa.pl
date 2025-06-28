from ..extensions import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    sender_id   = db.Column(db.Integer, db.ForeignKey("users.id"))
    receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    match_id    = db.Column(db.Integer, db.ForeignKey("matches.id"))
    message     = db.Column(db.Text)
    timestamp   = db.Column(db.DateTime, default=datetime.utcnow)
