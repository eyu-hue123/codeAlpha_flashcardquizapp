import json

def save_ticket(ticket):
    try:
        with open("data/tickets.json", "r") as f:
            tickets = json.load(f)
    except FileNotFoundError:
        tickets = []

    tickets.append(ticket)

    with open("data/tickets.json", "w") as f:
        json.dump(tickets, f, indent=2)
