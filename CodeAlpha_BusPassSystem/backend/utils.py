from datetime import datetime

valid_routes = {
    ("Adama", "Addis Ababa"): 100,
    ("Adama", "Dire Dawa"): 180,
    ("Adama", "Hawassa"): 150
}

def calculate_fare(origin, destination):
    return valid_routes.get((origin, destination), None)

def validate_date(date_str):
    try:
        travel_date = datetime.strptime(date_str, "%Y-%m-%d")
        return travel_date.date() >= datetime.now().date()
    except ValueError:
        return False
