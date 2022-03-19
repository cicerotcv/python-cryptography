import os
from pycrypto.keymanager import KeyManager
from .utils import split_input, store_key, write_file
from cryptography.fernet import Fernet


class Controller:
    @staticmethod
    def encrypt(data, key):
        fernet = Fernet(key=key)
        return fernet.encrypt(data=data)

    @staticmethod
    def decrypt(encrypted, password):
        if password is not None:
            key = KeyManager.generate(password)

        if key is not None:
            fernet = Fernet(key)
            return fernet.decrypt(encrypted)

        raise Exception("You must provide either 'password' or 'key'")

    @staticmethod
    def handle_output(args, key: bytearray, encrypted: bytearray):
        if args.input_mode == 'text':
            print(encrypted.content)
            print(f"Key:", key.decode())

        elif args.input_mode == 'file':
            dir, filename = split_input(args.filepath)

            key_filename = filename + '.key'
            filename = filename + '.pycrypted'

            key_path = os.path.join(dir, key_filename)
            data_path = os.path.join(dir, filename)

            write_file(key_path, key)
            write_file(data_path, encrypted)

            print(f"Key stored at '{key_path}'")
            print(f"Encrypted file stored at '{data_path}'")
