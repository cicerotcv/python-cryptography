# Python Cryptography

### Arguments

#### `$ python -m pytcrypt encrypt {text/file}`

```
# file
positional arguments:
filepath    Path of file to be encrypted
output      Output directory to store the encrypted file

optional arguments:
--store-key
            Whether the program should store the generated key or not
-p PASSWORD, --password PASSWORD
            Password used to decrypt
```

```
# text
positional arguments:
text        Text to be encrypted

optional arguments:
--store-key
            Whether the program should store the generated key or not
-p PASSWORD, --password PASSWORD
            Password used to decrypt
```

<!--
#### `$ python -m pytcrypt decrypt`

// To do

### Usage

```shell
# Encrypt a file
$ python -m pycrypto encrypt file input/dir/test.txt --store-key

File saved at 'output/dir/e_test.txt'
Key saved at 'output/dir/e_test.key'
```

```shell
# Encrypt a message
$ python -m pycrypto encrypt text "This is a message"

b''
``` -->
