from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass

passwd = getpass()
encrypt_message = raw_input("Masukan pesan : ")

cipher = b64decode(encrypt_message)
text = decrypt(passwd, cipher)
print("=====================")
print("isi pesan tersembunyi > " + text + "\n=====================")