import re

class InvalidEmailFormatError(Exception):
    def __init__(self, email):
        super().__init__(f" Invalid email format: {email}")
        self.email = email

def is_valid_email(email):
    # Basic regex for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

def validate_emails(email_list):
    invalid_emails = []

    for email in email_list:
        try:
            if not is_valid_email(email):
                raise InvalidEmailFormatError(email)
            print(f" Valid email: {email}")
        except InvalidEmailFormatError as e:
            print(e)
            invalid_emails.append(email)

    print("\nInvalid Emails Logged:")
    for bad_email in invalid_emails:
        print("-", bad_email)

# Example list of emails
emails = [
    "john.doe@example.com",
    "bademail@.com",
    "user123@domain",
    "good.email@site.org",
    "another_bad_email.com"
]

validate_emails(emails)
