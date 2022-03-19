import os
from random import shuffle
from string import hexdigits
from time import time


def split_input(path):
    dir = os.path.abspath(os.path.dirname(path))
    filename = os.path.basename(path)
    return dir, filename


def store_key(key: bytearray):
    filename = f"{int(time())}.key"
    path = os.path.join(os.path.curdir, filename)
    write_file(path, key)
    return path


def load_file(filepath: str) -> bytearray:
    with open(filepath, 'rb') as file:
        return file.read()


def write_file(filepath: str, content: bytearray):
    with open(filepath, 'wb+') as file:
        file.write(content)


def get_data(args):
    if args.input_mode == 'file':
        return load_file(args.filepath)

    if args.input_mode == 'text':
        return args.text.encode()
