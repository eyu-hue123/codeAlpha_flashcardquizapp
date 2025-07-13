from flask import Flask, request, jsonify
from encryptor import encrypt_data, decrypt_data
from validator import is_sql_safe
from access_manager import check_access
import json

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    code = data.get("capability")

    # Validate input
    if not is_sql_safe(email) or not is_sql_safe(password):
        return jsonify({"error": "SQL injection detected"}), 400

    role = check_access(code)
    if not role:
        return jsonify({"error": "Unauthorized access"}), 403

    encrypted_email = encrypt_data(email)
    encrypted_password = encrypt_data(password)

    # Simulate saving encrypted creds
    credentials = {
        "email": encrypted_email,
        "password": encrypted_password,
        "role": role
    }
    with open("data/users.json", "w") as f:
        json.dump(credentials, f, indent=2)

    return jsonify({"message": f"{role.capitalize()} logged in successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
