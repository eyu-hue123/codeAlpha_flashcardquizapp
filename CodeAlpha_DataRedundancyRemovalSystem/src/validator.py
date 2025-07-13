from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "name", "email"]
}

def is_valid(entry):
    try:
        validate(instance=entry, schema=schema)
        return True
    except ValidationError:
        return False
