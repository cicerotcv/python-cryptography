
from .utils import get_data
from .keymanager import KeyManager
from .commandparser import command_parser
from .controller import Controller


def main():
    args = command_parser()

    Controller.args = args

    if args.mode == 'encrypt':

        data = get_data(args)
        password = args.password
        key = KeyManager.generate(password)
        encrypted = Controller.encrypt(data, key)

        Controller.handle_output(args, key, encrypted)

    if args.mode == 'decrypt':
        Controller.decrypt()


if __name__ == '__main__':
    main()
