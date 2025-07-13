import json
from validator import is_valid
from deduplicator import remove_duplicates

def load_entries(path):
    with open(path) as f:
        return json.load(f)

def save_cleaned_entries(entries, out_path="data/cleaned_entries.json"):
    with open(out_path, "w") as f:
        json.dump(entries, f, indent=2)

def process_entries():
    raw_entries = load_entries("data/entries.json")
    valid_entries = [e for e in raw_entries if is_valid(e)]
    unique_entries = remove_duplicates(valid_entries)
    save_cleaned_entries(unique_entries)
    print(f"✅ {len(unique_entries)} unique entries saved.")

if __name__ == "__main__":
    process_entries()
