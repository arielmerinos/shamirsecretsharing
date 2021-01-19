import secrets
import hashlib
import os
import base64
from Crypto import Random as rnd
import Crypto.Cipher as AES
import getpass

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
    Verifica si un archivo se encuentra en un directorio
    """
    def verifica_archivo(archivo):
        directorio_raiz = "/home"  # solo en linux, en otro os?
        ruta = ""
        for i, _, archivos in os.walk(directorio_raiz):
            if archivo in archivos:
                ruta = os.path.join(i, archivo)
                break
        print(ruta)
        return ruta

    """
    Genera una lista de coeficientes de 256 bits para un polinomio de grado t-1 y el secreto
    """
    def coeficientes_del_polinomio(t, secreto):
        coeficientes = [Shamir.genera_coeficientes() for _ in range(t - 1)]
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


    """
    docstring
    """
    def encriptar(archivo):
        pass
    
    
    """
    la lista_argumentos : [archivo_por_cifrar, contrasenas_guardar, necesarios, evaluaciones]
    """
    def cifrar(lista_argumentos):
        try:
            archivo, contrasenas, necesarios, evaluaciones = lista_argumentos
            
            contrasena = getpass.getpass("Ingresa la contrseña para cifrar el archivo: ")
            """
            Nos encargamos de usar el algoritmo de hashing
            """
            contrasena = hashlib.sha256(contrasena.encode())
            
            K = int(contrasena.hexdigest(), 16)  # contrasena con sha y en decimales
            
            coeficientes = Shamir.coeficientes_del_polinomio(necesarios, K)
            coordenadas_evaluaciones = []
            for i in range(1, evaluaciones + 1):
                x = Shamir.genera_coeficientes()
                coordenadas_evaluaciones.append((x, Shamir.Metodo_de_Horner(x, coeficientes)))

            archivo_validado = Shamir.verifica_archivo(contrasenas)
            guardar_evaluciones = open(archivo_validado, "w")
            for coordenada in coordenadas_evaluaciones:
                guardar_evaluciones.write(str(coordenada))
            guardar_evaluciones.close()
            return guardar_evaluciones
        except FileNotFoundError:
            print("El archivo "+contrasenas+" no existe")
    
    def descrifrar():
        a = 1
        pass