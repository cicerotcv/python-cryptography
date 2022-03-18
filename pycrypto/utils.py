import os


def split_input(path):
    dir = os.path.abspath(os.path.dirname(path))
    filename = os.path.basename(path)
    return dir, filename


def load_file(filepath: str):
    with open(filepath, 'rb') as file:
        return file.read()


def get_message(args):
    if args.input_mode == 'file':
        return load_file(args.filepath)

    if args.input_mode == 'text':
        return args.text.encode()
