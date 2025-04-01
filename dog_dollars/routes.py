from flask import Blueprint, request, jsonify

dog_dollars_bp = Blueprint("dog_dollars", __name__)

@dog_dollars_bp.route("/generate", methods=["POST"])
def generate():
    # Replace this with your real logic
    return jsonify({"code": "DOG10", "status": "generated"})
