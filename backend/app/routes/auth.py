from flask import request, jsonify
from flask_jwt_extended import create_access_token
from ..models import User
from ..extensions import db
from . import auth_bp

@auth_bp.post("/register")
def register():
    data = request.json
    user = User(
        name=data["name"], email=data["email"], age=data.get("age"),
        description=data.get("description")
    )
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(msg="ok"), 201

@auth_bp.post("/login")
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user or not user.check_password(data["password"]):
        return jsonify(msg="bad creds"), 401
    token = create_access_token(identity=user.id)
    return jsonify(access_token=token)
