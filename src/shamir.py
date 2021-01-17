import secrets
import hashlib
import base64
from Crypto import Random as rnd
import Crypto.Cipher as AES
import getpass
import Encripta
class Shamir:
    
    _primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481
    pad = lambda s: s + (32 - len(s) % 32) * chr(32 - len(s) % 32)
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    


    """
    Genera numéros aletorioss de 256 bits, siempre encargándose de que dicho número sea menor al módulo primo
    """
    def genera_coeficientes():
        numero_aleatorio = secrets.randbits(256)
        
        while(numero_aleatorio > Shamir._primo):
            numero_aleatorio = secrets.randbits
            
        return numero_aleatorio
    
    """
    Se encarga de encriptar un archivo y pedir la contrase-a
    """
    def encode_contrasena():
        contrasena = getpass.getpass("Ingresa la contrseña para cifrar el archivo: ")
        contrasena = hashlib.sha256(contrasena.encode()).digest()
        print(contrasena)
        return contrasena

    
    
    """
    la lista_argumentos : [archivo_por_cifrar, contrasenas_guardar, necesarios, evaluaciones]
    """
    def cifrar(lista_argumentos):
        archivo, contrasenas, necesarios, evaluaciones = lista_argumentos
        key = Shamir.encode_contrasena()
        
        enc = Encripta(key)
        enc.encrypt_file(archivo)
        print(key)
        
        
        pass
    
    def descrifrar():
        a = 1
        pass