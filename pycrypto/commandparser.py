import argparse



def command_parser():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='mode')

    encryption_group = subparser.add_parser(name="encrypt", help="Encrypt a file or message")    
    input_mode = encryption_group.add_subparsers(dest='input_mode')
    
    # Input mode is "file"
    file_mode = input_mode.add_parser(name="file", help="Input a file to be encrypted")
    file_mode.add_argument(dest="filepath", help="Path of file to be encrypted")
    file_mode.add_argument('--store-key', dest="store_key", help="Whether the program should store the generated key or not")

    # Input mode is "text"
    text_mode = input_mode.add_parser(name="text", help="Encrypt the following text") 
    text_mode.add_argument(dest="text", help="Text to be encrypted")

    encryption_group.add_argument('-p', '--password', help="Password used to decrypt")

    return parser.parse_args()
