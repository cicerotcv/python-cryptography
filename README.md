# Python Cryptography

### Arguments

#### `$ python -m pytcrypt encrypt`

```
# file
positional arguments:
filepath    Path of file to be encrypted
output      Output directory to store the encrypted file

# text
positional arguments:
text        Text to be encrypted
```

#### `$ python -m pytcrypt decrypt`

// To do

### Usage

```shell
# Encrypt a file
$ python -m pycrypto encrypt file input/dir/test.txt -o output/dir/

File saved at 'output/dir/e_test.txt'
Key saved at 'output/dir/e_test.key'
```

```shell
# Encrypt a message
$ python -m pycrypto encrypt text "This is a message"

b''
```
