from flask import Blueprint, request, jsonify
import os
from datetime import datetime

dog_dollars_bp = Blueprint("dog_dollars", __name__)

@dog_dollars_bp.route("/generate-code", methods=["POST"])
def generate_code():
    data = request.get_json()
    customer_id = data.get("customer_id")
    order_id = data.get("order_id")

    if not customer_id or not order_id:
        return jsonify({"error": "Missing customer_id or order_id"}), 400

    code = f"DOG-{customer_id[:4]}-{order_id[-4:]}"
    timestamp = datetime.utcnow().isoformat()

    return jsonify({
        "code": code,
        "created": timestamp
    })
