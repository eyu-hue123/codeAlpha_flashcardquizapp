import re

def is_sql_safe(input_text):
    # Common injection patterns
    blacklist = [r"('|--|\bOR\b|\bAND\b|\bDROP\b|\bSELECT\b|\bDELETE\b|\bINSERT\b|\bUPDATE\b)"]
    for pattern in blacklist:
        if re.search(pattern, input_text, re.IGNORECASE):
            return False
    return True
