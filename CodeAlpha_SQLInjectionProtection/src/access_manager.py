# Simulated access codes
valid_capability_codes = {
    "admin123": "admin",
    "user456": "user"
}

def check_access(code):
    return valid_capability_codes.get(code, None)
