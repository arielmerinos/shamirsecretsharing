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
        #print(coeficientes)
        return coeficientes

    """
    Evalúa un polinomio dado "x" y una lista de los coeficientes del mismo con el método de Horner
    """
    def Metodo_de_Horner(self,x,coeficientes):
        resultado = coeficientes[0]
        for i in range(1, len(coeficientes)):
            resultado = resultado * x + coeficientes[i]
        #print(resultado)
        return resultado % Shamir._primo


    """
    docstring
    """
    def encriptar(archivo):
        pass
    
    
    """
    la lista_argumentos : [archivo_por_cifrar, contrasenas_guardar, necesarios, evaluaciones]
    """
    def cifrar(self, lista_argumentos):
        archivo, contrasenas, necesarios, evaluaciones = lista_argumentos
        #contrasena = getpass.getpass("Ingresa la contrseña para cifrar el archivo: ")
        contrasena = "Armando"
        contrasena = hashlib.sha256(contrasena.encode())
        K = int(contrasena.hexdigest(), 16)  # contrasena con sha y en decimales
        coeficientes = self.coeficientes_del_polinomio(necesarios, K)
        coordenadas_evaluaciones = []
        for i in range(1,evaluaciones + 1):
            x = self.genera_coeficientes()
            coordenadas_evaluaciones.append([x, self.Metodo_de_Horner(x, coeficientes)])
        print(coordenadas_evaluaciones)
        return  coordenadas_evaluaciones
        #pass
    
    def descrifrar():
        a = 1
        pass