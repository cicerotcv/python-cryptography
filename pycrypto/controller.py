from .cryptomanager import Cryptography
from .utils import get_message


class Controller:
    @staticmethod
    def encrypt(args):
        data = get_message(args)
        password = args.password

        key, encrypted = Cryptography.encrypt(data, password)

        Controller.handle_output(args=args, data=encrypted, key=key)

    @staticmethod
    def decrypt(args):
        pass

    @staticmethod
    def handle_output(args, data, key):
        # to do
        print(data)
        print(key)
