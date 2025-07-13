from flask import Flask, request, jsonify
from utils import calculate_fare, validate_date
from database import save_ticket

app = Flask(__name__)

@app.route("/book", methods=["POST"])
def book_ticket():
    data = request.json
    name = data.get("name")
    origin = data.get("origin")
    destination = data.get("destination")
    date = data.get("travel_date")
    payment = data.get("payment_method")

    if not all([name, origin, destination, date, payment]):
        return jsonify({"error": "Missing required fields"}), 400

    if not validate_date(date):
        return jsonify({"error": "Invalid travel date"}), 400

    fare = calculate_fare(origin, destination)
    if fare is None:
        return jsonify({"error": "Invalid route"}), 400

    ticket = {
        "name": name,
        "origin": origin,
        "destination": destination,
        "travel_date": date,
        "payment_method": payment,
        "fare": fare
    }

    save_ticket(ticket)
    return jsonify({"message": "🎟️ Ticket booked successfully", "ticket": ticket})

if __name__ == "__main__":
    app.run(debug=True)
