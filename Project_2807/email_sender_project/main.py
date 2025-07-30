from emailer.email_sender import Email

def load_template(file_path, **kwargs):
    with open(file_path, "r") as f:
        content = f.read()
        return content.format(**kwargs)

if __name__ == "__main__":
    body = load_template("templates/sample_template.txt", name="User")
    email = Email(
        subject="Test Email from Python",
        body=body,
        recipients=["suganyasdv16@gmail.com"],
        attachments=["requirements.txt"]
    )
    email.send()
