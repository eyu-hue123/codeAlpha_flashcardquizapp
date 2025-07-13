from flask import Flask, request, jsonify
from logic import get_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    reply = get_response(user_input)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
