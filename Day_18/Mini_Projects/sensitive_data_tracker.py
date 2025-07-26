import datetime

class SecureData:
    def __init__(self, secret):
        self._secret = secret

    @property
    def secret(self):
        # Log access
        timestamp = datetime.datetime.now().isoformat()
        print(f"[ACCESS LOG] Secret accessed at {timestamp}")
        return self._secret

    @secret.setter
    def secret(self, value):
        raise AttributeError("Write access to 'secret' is denied!")

if __name__ == "__main__":
    user_data = SecureData("TopSecret123")

    # Access the secret (read-only)
    print("Reading secret:", user_data.secret)

    # Try modifying the secret
    try:
        user_data.secret = "NewSecret!"
    except AttributeError as e:
        print("Error:", e)
