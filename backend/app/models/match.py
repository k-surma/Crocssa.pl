from ..extensions import db
from datetime import datetime

class Match(db.Model):
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user2_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    matched_at = db.Column(db.DateTime, default=datetime.utcnow)
