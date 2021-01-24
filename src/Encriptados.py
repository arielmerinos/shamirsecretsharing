from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
import hashlib
"""
Esta clase está diseñada para interactuar con AES, exclusivamente en encriptar y desencriptar archivos
"""
class Encriptador:
    def __init__(self, key):
        self.key = key

    """
    Normaliza el tamaño de los bloques a 32 bytes
    """
    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

        
    """
    Se encarga de encriptar un flujo de información
    """
    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    """
    Toma un archivo desde la ruta proporcionada y lo cifra haciendo uso del método encrypt
    """
    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    """
    Dada una contraseña y un bloque de texto cifrado se encarga de descifrar la cadena
    """
    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    """
    Se encarga de desencriptar el archivo cifrado haciendo uso del método decrypt
    """
    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)
        
    """
    Este método busca pasar de una llave decimal a auna llave en bytes para administrase en descifrar 
    """
    def convierte_llave(self, llave):
        return hashlib.sha256(llave).digest()

