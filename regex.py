import re

# An example text
text = "The quick brown fox jumps over 2025 lazy dogs. Contact: bipin@gmail.com"

# Finding all digits
digits = re.findall(r'\d+', text)
print("Digits found:", digits)

# Finding any email pattern in text
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print("Emails found:", emails)

# Search and matching
phone_text = "Call me at 123-456-7890 or 987-654-3210"
phone_pattern = r'\d{3}-\d{3}-\d{4}'
first_phone = re.search(phone_pattern, phone_text)
all_phones = re.findall(phone_pattern, phone_text)

if first_phone:
    print("First phone found:", first_phone.group())
print("All phones:", all_phones)

# Substitution with a number in the string
censored = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', phone_text)
print("Censored text:", censored)

# Groups and capturing
log_line = "2025-09-26 14:30:22 ERROR Failed to connect"
log_pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)'
match = re.match(log_pattern, log_line)

if match:
    date, time, level, message = match.groups()
    print(f"Date: {date}, Time: {time}, Level: {level}, Message: {message}")

# Named groups
email_pattern_named = r'(?P<username>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})'
email_match = re.search(email_pattern_named, text)
if email_match:
    print("Username:", email_match.group('username'))
    print("Domain:", email_match.group('domain'))

# Creating a validation function using regex
def validate_input(text, pattern_type):
    """Validate different types of input using regex"""
    patterns = {
        'email': r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$',
        'phone': r'^\d{3}-\d{3}-\d{4}$',
        'zipcode': r'^\d{5}(-\d{4})?$',
        'url': r'^https?://(www\.)?[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}(/.*)?$'
    }
    
    pattern = patterns.get(pattern_type)
    if pattern:
        return bool(re.match(pattern, text))
    return False

# Validating a bunch of string types
test_inputs = [
    ("bipin@gmail.com", "email"),
    ("123-456-7890", "phone"),
    ("12345", "zipcode"),
    ("https://www.google.com", "url")
]

for text, pattern_type in test_inputs:
    result = validate_input(text, pattern_type)
    print(f"'{text}' is valid {pattern_type}: {result}")

