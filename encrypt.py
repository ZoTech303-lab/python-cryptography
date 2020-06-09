import sys
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass

passwd = getpass()
encrypt_message = raw_input("Masukan Pesan : ")

print("=========================")
print("Sedang mengenkripsi pesan > " + encrypt_message)
print("=========================")

cipher = encrypt(passwd, encrypt_message)
encode_cipher = b64encode(cipher)
print("========================")
print("Pesan telah ter enkripsi > " + encode_cipher)
print("========================")