import hashlib


class Hasher:
    def __init__(self):
        # Create a SHA256 hash object
        self.sha256_hash = hashlib.sha256()
        pass

    def sha256(self, text: str):
        # Encode the text as bytes
        text_bytes = text.encode("utf-8")
        # Update the hash with the text bytes
        self.sha256_hash.update(text_bytes)
        # Get the hexadecimal digest of the hash
        hex_digest = self.sha256_hash.hexdigest()
        return hex_digest
