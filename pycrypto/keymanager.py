import base64
from os import urandom
from typing import Union

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class KeyManager:
    @staticmethod
    def generate(password: Union[str, None]):
        if password is None:
            return Fernet.generate_key()
        

        password = password.encode()

        salt = password + urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=salt,
                         iterations=1000,
                         backend=default_backend())
        return base64.urlsafe_b64encode(kdf.derive(password))
