from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os


class Encryptor:

    def __init__(self):
        self.key = 0

    def set_key(self, key):
        self.key = key

    def encrypt(self, message, key):
        padded_message = pad(message,AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(padded_message)
        return iv + ciphertext

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as file:
            plaintext = file.read()
        enc = self.encrypt(plaintext, self.key)
        with open("enc_" + file_name, 'wb') as file:
            file.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        plaintext = unpad(padded_plaintext,AES.block_size)
        return plaintext

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as file:
            ciphertext = file.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[4:], 'wb') as file:
            file.write(dec)
        os.remove(file_name)
