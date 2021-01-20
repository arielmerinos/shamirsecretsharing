import math
import random
class InterpolacionLagrange:
    _primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481
    
    def get_inverso(num):
        NUM = num
        modulito = InterpolacionLagrange._primo
        x, x_old = 0, 1

        y, y_old = 1, 0

        while InterpolacionLagrange._primo:

            q = num // InterpolacionLagrange._primo

            num, InterpolacionLagrange._primo = InterpolacionLagrange._primo, num % InterpolacionLagrange._primo

            x, x_old = x_old - q * x, x

            y, y_old = y_old - q * y, y

        if num != 1:

            print("\nNO MI. However, the GCD of %d and %d is %u\n" % (NUM, InterpolacionLagrange._primo, num))

        else:
            
            inverso = (x_old + InterpolacionLagrange._primo) % InterpolacionLagrange._primo
            #print("\nMI of %d modulo %d is: %d\n" % (NUM, MOD, MI))
            return inverso
    
    """
    Método para obtener los Li de la ecuación del método de interpolación de Lagrange
    @param: x_i
    @param: array coeficientes en X
    @return: Polinomio Li(x)
    """
    def li(i_i, coeficientes_x):

        denominador = 1
        numerador = 1

        for j in range(0, len(coeficientes_x)):

            if(int(coeficientes_x[j]) != int(i_i)):

                numerador *= int(-coeficientes_x[j])

                denominador *= int(i_i-coeficientes_x[j])

        numerador = numerador % InterpolacionLagrange._primo


        denominador = InterpolacionLagrange.get_inverso(denominador % InterpolacionLagrange._primo)

        return (numerador * denominador) % self._primo
    '''
    Método principal para el polinomio de Lagrange
    @param: vector con las x_i
    @param: vector con las y_i
    @return: Polinomio de lagrange generado por la intepolación
    '''
    def lagrangeCero(self, x_i, y_i): # vectores = [(0, 1), (1, 3), (2, 0)]
        suma = 0

        for i in range(0, len(x_i)):

            pol = InterpolacionLagrange.li(x_i[i], x_i) % self._primo
            y_i[i] = y_i[i] % self._primo 
            producto = (pol * y_i[i]) % self._primo

            suma += producto

        return suma % self._primo