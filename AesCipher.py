import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key):
        self.blockSize = 32
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, cipherMessage):
        cipherMessage = base64.b64decode(cipherMessage)
        iv = cipherMessage[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(cipherMessage[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.blockSize - len(s) % self.blockSize) * chr(self.blockSize - len(s) % self.blockSize).encode('utf-8')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
