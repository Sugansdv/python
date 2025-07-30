import base64
import hashlib

def generate_fernet_key(secret: str) -> bytes:
    """Convert user string to Fernet-compatible key (32-byte base64)"""
    hash_digest = hashlib.sha256(secret.encode()).digest()
    return base64.urlsafe_b64encode(hash_digest)
