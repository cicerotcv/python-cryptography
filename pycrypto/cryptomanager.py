
from cryptography.fernet import Fernet

from pycrypto.keymanager import KeyManager


class Cryptography:

    @staticmethod
    def encrypt(data, password):
        key = KeyManager.generate(password)
        fernet = Fernet(key=key)
        encrypted_content = fernet.encrypt(data=data)
        return key, encrypted_content

    @staticmethod
    def decrypt(encrypted_data, password=None, key=None):
        if password is not None:
            key = KeyManager.generate(password)

        if key is not None:
            fernet = Fernet(key)
            return fernet.decrypt(encrypted_data)

        raise Exception("You must provide either 'password' or 'key'")
