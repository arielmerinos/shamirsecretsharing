
class InterpolacionLagrange:
    _primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481

    """
    Este método calcula el inverso de un número en un Zp
    """
    def inverso_perro(self, numero):
        modulo = self._primo
        NUM = numero
        MOD = self._primo
        x, x_original = 0, 1
        y, y_original = 1, 0
        while modulo:
            div = numero // modulo
            numero, modulo = modulo, numero % modulo
            x, x_original = x_original - div * x, x
            y, y_original = y_original - div * y, y
        if numero != 1:
            pass
        else:
            res = (x_original + MOD) % MOD
            return res

    """
    Método para obtener los Li de la ecuación del método de interpolación de Lagrange
    @param: x_i
    @param: array coeficientes en X
    @return: Polinomio Li(x)
    """

    def elementos_multiplicat(self,i_i, coeficientes_x):

        denominador = 1
        numerador = 1

        for j in range(0, len(coeficientes_x)):

            if (int(coeficientes_x[j]) != int(i_i)):
                numerador *= int(-coeficientes_x[j])

                denominador *= int(i_i - coeficientes_x[j])

        numerador = numerador % self._primo

        denominador = self.inverso_perro(denominador % self._primo)

        return (numerador * denominador) % self._primo

    '''
    Método principal para el polinomio de Lagrange
    @param: vector con las x_i
    @param: vector con las y_i
    @return: Polinomio de lagrange generado por la intepolación
    
    
    PARA PRUEBAAAAAAAAAS
    x _i =[1, 3, 7]
    y_i = [17, 65, 221]
    '''

    def lagrangeCero(self, x_i, y_i):  # vectores = [(0, 1), (1, 3), (2, 0)]
        suma = 0

        for i in range(0, len(x_i)):
            pol = self.elementos_multiplicat(x_i[i], x_i) % self._primo
            y_i[i] = y_i[i] % self._primo
            producto = (pol * y_i[i]) % self._primo

            suma += producto

        return suma % self._primo
