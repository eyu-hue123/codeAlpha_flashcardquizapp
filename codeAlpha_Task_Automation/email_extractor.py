import re

# Read input file
with open("sample.txt", "r") as file:
    content = file.read()

# Regex pattern to extract emails
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

# Save to output file
with open("extracted_emails.txt", "w") as output:
    for email in emails:
        output.write(email + "\n")

print(f" {len(emails)} email(s) extracted and saved to 'extracted_emails.txt'.")