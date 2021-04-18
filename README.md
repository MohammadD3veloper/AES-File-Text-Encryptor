# AES-File-Text-Encryptor
A tool for fast and ez file/text encryption with AES Mode CBC algorithm 

# How to use it?
simply clone the repo using:

`git clone https://github.com/DrD3ViLaM/AES-File-Text-Encryptor.git`

then cd into cloned directory:

`cd AES-File-Text-Encryptor`

then just enter commands below:

`pip install -r requirements.txt`

`chmod +x run.py`

`./run.py`

# How to use it as a module ?

at first you should import FileEncryptor class like this:

```from encryptor import FileEncryptor```

then create an instance of it and pass arguments like:

```instance = FileEncryptor(key='abcdefghijklmnop'.encode(),size=128,iv='abcdefghijklmnop'.encode())```

then simply use methods:

## Encrypt text

```encrypted = instance.encrypttext("A Message")```

```print(encrypted)```

## Decrypt text

```decrypted = instance.encrypttext(encrypted)```

```print(decrypted)```

and more methods are available in encryptor.py you can check how to use them from run.py
