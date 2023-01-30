import base64
import hashlib
from AesCipher import AESCipher

class Encrypter:
    def __init__(self,key, message):
        self.Key = key
        self.Message = message

    def encrypt(self):
        aes = AESCipher(self.Key)
        cipherMessage = aes.encrypt(self.Message)
        return cipherMessage