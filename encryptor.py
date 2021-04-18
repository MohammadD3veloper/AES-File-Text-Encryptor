# Module aes encryptor 
# Author : Dr.D3ViLaM
# Written in : Python
# License GPL


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from os import path as p, listdir, remove
from base64 import b64decode, b64encode
from os import urandom

"""
* AES File Text Encryptor 
   * A tool for encryptig files/texts with AES MODE CBC *
   * Written in Python Programming Language             *
   * Author : Dr.D3ViLaM                                *
   * Contact me on T.me/DrD3ViLaM                       *
"""

class FileEncryptor:

    iv = "adefault16bitsiv".encode()
    key128 = urandom(16)
    key192 = urandom(24)
    key256 = urandom(32)

    size128 = 128
    size192 = 192
    size256 = 256


    def __init__(self, key:bytes, size:int , iv:bytes):
        """
        You can use default values for keys, iv, size from FileEncryptor
        or
        give a key 16/24/32 bits | if key eq 16:size must be 128 - if key eq 24:size must be 192 - if key eq 32:size must be 256
        give an 16 bits iv 
        """

        self.key = key
        self.size = size
        self.iv = iv

    def __str__(self):
        return "AES File/Text Encryptor wrote by : Dr.D3ViLaM and Python language"
    

    def encryptfile(self, file_name:str) -> bool:
        """
        file_name argument as string.
        return True for success | False for faild
        """

        encryptor = AES.new(self.key, mode=AES.MODE_CBC, iv=self.iv)
        with open(file_name,'rb') as fo:
            text = fo.read()
            hx = encryptor.encrypt(pad(text,block_size=AES.block_size))
            bs64 = b64encode(hx)
            fo.close()

        with open(file_name + ".D3ViLcrypt",'wb') as fr:
            fr.write(bs64)
            fr.close()
            
        remove(file_name)
        return 1



    def decryptfile(self, file_name:str) -> bool:
        """
        file_name argument as string.
        return True for success | False for faild
        """
        decryptor = AES.new(self.key, mode=AES.MODE_CBC, iv=self.iv)
        if ".D3ViLcrypt" in file_name:
            file_n = list(file_name)
            del file_n[-11:-1]
            file_n.pop()
            file_name = "".join(file_n)

        with open(file_name + ".D3ViLcrypt" , 'r') as fo:
            text = fo.read()
            deb64 = b64decode(text)
            x=decryptor.decrypt(deb64)
            unpadded = unpad(x,AES.block_size)
            plain_text = unpadded.decode()
            fo.close()

        with open(file_name, "w") as fr:
            fr.write(plain_text)
            fr.close()

        remove(file_name + ".D3ViLcrypt")
        return 1
    

    def encryptfiles(self, path:str) -> bool:
        "Encrypt all files in a directory"
        if p.exists(path):
            files = listdir(path)
            for f in files:
                if self.encryptfile(path + '/' + f) == True:
                    print(f"{f} Encrypted.")
            return 1

        else:
            raise Exception("No such directory in path.")
            return 0


    def decryptfiles(self, path:str) -> bool:
        "Decrypt all files in a directory"
        if p.exists(path):
            files = listdir(path)
            for f in files:
                if self.decryptfile(path + '/' + f) == True:
                    print(f"{f} Decrypted.")

        else:
            raise Exception("No Such Directory in path")

    def encrypttext(self, message:str) -> str:
        """
        Encrypt message u give it as an argument then it will return as a base64 cipher
        """
        encryptor = AES.new(self.key, mode=AES.MODE_CBC, iv=self.iv)
        hx = encryptor.encrypt(pad(message.encode(),AES.block_size))
        return b64encode(hx).decode()


    def decrypttext(self, cipher:str) -> str:
        """
        Decrypt ciphertext u give it as an argument then it will return as a string plaintext
        """
        decryptor = AES.new(self.key, mode=AES.MODE_CBC, iv=self.iv)
        deb64 = b64decode(cipher)
        x=decryptor.decrypt(deb64)
        unpadded = unpad(x,AES.block_size)
        return unpadded.decode()