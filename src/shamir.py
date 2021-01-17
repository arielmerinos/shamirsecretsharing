import secrets
import pyaes
import hashlib
import getpass

class Shamir:
    _primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481

    """
    Genera numéros aletorioss de 256 bits, siempre encargándose de que dicho número sea menor al módulo primo
    """
    def genera_coeficientes(self):
        numero_aleatorio = secrets.randbits(256)
        
        while(numero_aleatorio > Shamir._primo):
            numero_aleatorio = secrets.randbits
            
        return numero_aleatorio

    """
    Genera una lista de coeficientes de 256 bits para un polinomio de grado t-1 y el secreto
    """
    def coeficientes_del_polinomio(self,t, secreto):
        coeficientes = [self.genera_coeficientes() for _ in range(t - 1)]
        coeficientes.append(secreto)
        print(coeficientes)

    """
    docstring
    """
    def encriptar(archivo):
        pass
    
    
    """
    la lista_argumentos : [archivo_por_cifrar, contrasenas_guardar, necesarios, evaluaciones]
    """
    def cifrar(lista_argumentos):
        archivo, contrasenas, necesarios, evaluaciones = lista_argumentos

        contrasena = getpass.getpass("Ingresa la contrseña para cifrar el archivo: ")
        contrasena = hashlib.sha256(contrasena.encode())
        K = int(contrasena.hexdigest(), 16)  # contrasena con sha y en decimales
        
        pass
    
    def descrifrar():
        a = 1
        pass