 def remove_duplicates(entries):
    unique = []
    seen_ids = set()
    for entry in entries:
        if entry["id"] not in seen_ids:
            unique.append(entry)
            seen_ids.add(entry["id"])
    return unique
