#!/usr/bin/python

"""
* AES File Text Encryptor *
   * A tool for encryptig files/texts with AES MODE CBC *
   * Written in Python Programming Language             *
   * Author : Dr.D3ViLaM                                *
   * Contact me on T.me/DrD3ViLaM                       *
"""

from encryptor import FileEncryptor
from colorama import Fore, Back,init
from logging import error, warning
from sys import exit, stdout
from getpass import getuser
from os import system


init(autoreset=True)


def main():
    system("clear")
    print(Fore.RED+Back.BLACK+"""
AES-Encryptor                |                    Dr.D3ViLaM
==== ================================================== ====
   * A tool for encryptig files/texts with AES MODE CBC *
   * Written in Python Programming Language             *
   * Author : Dr.D3ViLaM                                *
   * Contact me on T.me/DrD3ViLaM                       *
==== ================================================== ====
    """)
    try:
        size = int(input("[?] Select your AES CBC size >\n\n1) 128\n2) 192\n3) 256\n\nEnter -> "))
        if size == 1:
            size = 128
            def_key = FileEncryptor.key128
        elif size == 2:
            size = 192
            def_key = FileEncryptor.key192
        elif size ==3:
            def_key = FileEncryptor.key256
            size = 256
        else:
            error(Fore.RED + f"Value must be 1/2/3 not {size}")
            exit(-1)


        key = input("Enter key or press [ENTER] for default key -> ")
        if key == '':
            warning(Fore.YELLOW+"[WARNING] : Default key values will be destroy after closing app because they are generate randomly\nIf your data is sensitive and you need to access them after days use your own key")
            key = def_key

        elif len(key) != 16 or len(key) != 24 or len(key) != 32:
            error(f"key must be 16/24/32, not {key}")
            exit(-1)
        else:
            key = key.encode()

        iv = input("Enter iv or press [Enter] for default iv -> ")
        if iv == '':
            iv = FileEncryptor.iv

        elif len(iv) != 16:
            error(Fore.RED+f"Invalid IV: Iv must be equal 16, not {iv}")

        else:
            iv = iv.encode()

        wdid = int(input("How can I help you? \n\n1) Encrypt text\n2) Decrypt text \n3) Encrypt File\n4) Encrypt Files\n5) Decrypt File\n6) Decrypt Files\n\nEnter -> "))
        if wdid == 1:
            msg = input("Enter text -> ")
            hcihy = FileEncryptor(key, size, iv)
            print(hcihy.encrypttext(msg))

        elif wdid == 2:
            ciph = input("Enter Cipher -> ")
            hcihy = FileEncryptor(key, size, iv)
            print(hcihy.decrypttext(ciph))

        elif wdid == 3:
            file_name = input("Enter filename -> ")
            hcihy = FileEncryptor(key, size, iv)
            if hcihy.encryptfile(file_name) == True:
                print(Fore.GREEN+"Success.")

        elif wdid == 4:
            files = input("Enter path of your directory -> ")
            hcihy = FileEncryptor(key, size, iv)
            if hcihy.encryptfiles(files) == True:
                print(Fore.GREEN+"Success.")

        elif wdid == 5:
            file_name = input("Enter filename (without encrypted format) -> ")
            hcihy = FileEncryptor(key, size, iv)
            if hcihy.decryptfile(file_name) == True:
                print("Done.")

        elif wdid == 6:
            files = input("Enter path of your directory -> ")
            hcihy = FileEncryptor(key, size, iv)
            if hcihy.decryptfiles(files) == True:
                print("Done.")

        else:
            error(Fore.RED + "[!] Wrong value entered")
            exit(-1)
    except KeyboardInterrupt:
            warning(Fore.RED + f"Aborted by user : {getuser()}")


if __name__ == "__main__":
    main()
