import base64
import hashlib
from AesCipher import AESCipher

class Decrypter:
    def __init__(self,key, message):
        self.Key = key
        self.Message = message

    def decrypt(self):
        aes = AESCipher(self.Key)
        decipherMessage = aes.decrypt(self.Message)
        base64_decoded = aes.decrypt(self.Message)
        fh = open("decryptedImage.png", "wb")
        fh.write(base64.b64decode(base64_decoded))
        fh.close()
        return (base64.b64decode(base64_decoded))