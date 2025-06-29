import os, uuid
from flask import Blueprint, request, jsonify, send_from_directory, current_app
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename

upload_bp = Blueprint("upload", __name__, url_prefix="/api")

ALLOWED = {"png", "jpg", "jpeg", "gif"}

def allowed(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED

@upload_bp.post("/upload")
@jwt_required()
def handle_upload():
    if "file" not in request.files:
        return jsonify(msg="missing file"), 400
    f = request.files["file"]
    if not allowed(f.filename):
        return jsonify(msg="bad filetype"), 400

    ext   = f.filename.rsplit(".", 1)[1].lower()
    name  = secure_filename(f"{uuid.uuid4().hex}.{ext}")
    path  = os.path.join(current_app.config["UPLOAD_FOLDER"], name)
    f.save(path)

    url = f"/uploads/{name}"
    return jsonify(url=url), 201

# ─── statyczne serwowanie ────────────────────────────────────────────────
@upload_bp.get("/uploads/<path:fname>")
def uploaded_file(fname):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], fname)
