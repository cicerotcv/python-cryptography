
from .commandparser import command_parser
from .controller import Controller


def main():
    args = command_parser()

    if args.mode == 'encrypt':
        Controller.encrypt(args)

    if args.mode == 'decrypt':
        Controller.decrypt(args)


if __name__ == '__main__':
    main()
