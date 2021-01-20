import secrets
import hashlib
import os
import random
from decimal import *
import base64
from Crypto import Random as rnd
import Crypto.Cipher as AES
import getpass
from Encriptados import Encriptador

class Shamir:
    
    _primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481
    pad = lambda s: s + (32 - len(s) % 32) * chr(32 - len(s) % 32)
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    """
    Genera numéros aletorioss de 256 bits, siempre encargándose de que dicho número sea menor al módulo primo y que no sea 0
    """
    def genera_coeficientes():
        numero_aleatorio = secrets.randbits(256)
        
        while(numero_aleatorio > Shamir._primo and numero_aleatorio == 0):
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
    Genera una lista de coeficientes de 256 bits para un polinomio de grado t-1 y el secreto
    """
    def coeficientes_del_polinomio(t, secreto):
        coeficientes = [Shamir.genera_coeficientes() for _ in range(t-1)]
        coeficientes.append(secreto)
        return coeficientes

    """
    Evalúa un polinomio dado "x" y una lista de los coeficientes del mismo con el método de Horner
    """
    def Metodo_de_Horner(x,coeficientes):
        resultado = coeficientes[0]
        for i in range(1, len(coeficientes)):
            resultado = (((resultado * x) % Shamir._primo) + coeficientes[i]) % Shamir._primo
        return resultado

    
    def escribir_txt(lista, archivo):
        modo = 'a' if os.path.exists(archivo) else 'w+'
        archivo = open(archivo, modo)
        for elemento in lista:
            archivo.write(str(elemento)+"\n")
        archivo.close()
        
        
    """
    la lista_argumentos : [archivo_por_cifrar, contrasenas_guardar, necesarios, evaluaciones]
    """
    def cifrar(lista_argumentos):

        archivo, contrasenas, necesarios, evaluaciones = lista_argumentos
        
        contrasena = getpass.getpass("Ingresa la contrseña para cifrar el archivo: ")
       
        """
        Nos encargamos de usar el algoritmo de hashing
        """
        contrasena = hashlib.sha256(contrasena.encode())
        
        """
        Se encarga de encriptar el archivo q fantasía
        """
        enc = Encriptador(contrasena.digest())
        enc.encrypt_file(archivo)
        
        
        K = int(contrasena.hexdigest(), 16)  # contrasena con sha y en decimales
        coeficientes = Shamir.coeficientes_del_polinomio(necesarios, K)
        print(K)
        coordenadas_evaluaciones = []
        for i in range(1, evaluaciones + 1):
            punto_aleatorio = Shamir.genera_coeficientes()
            coordenadas_evaluaciones.append((punto_aleatorio, Shamir.Metodo_de_Horner(punto_aleatorio, coeficientes)))

        Shamir.escribir_txt(coordenadas_evaluaciones, contrasenas)
    
    def descrifrar(lista_argumentos):
        archivo_descifrar, contresenas = lista_argumentos
        archivo = open(contresenas, "r")
        leer_archivo = archivo.read()
        cadena_contrasenas = leer_archivo.splitlines()
        archivo.close()

        lista_contrasenas = [eval(elemento) for elemento in cadena_contrasenas]
        t = random.randrange(2, len(lista_contrasenas))
        necesarios_secreto_original = random.sample(lista_contrasenas, t)

        print(necesarios_secreto_original)
        print(len(necesarios_secreto_original))



