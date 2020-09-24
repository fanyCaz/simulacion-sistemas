from fractions import Fraction

def numRectMultiplicativos(x0: int,a: int,m: int):
    #Periodo Esperado
    PE  = int(m/4)
    xn  :int = x0
    numRectangular :int = 0
    numerosRectangulares = []
    #Formula ax0 mod m
    for i in range(PE):
        fraccion = Fraction((a*xn)/m)
        z = fraccion.numerator
        while(z > fraccion.denominator):
            z -= fraccion.denominator
        numRectangular = Fraction(z,fraccion.denominator)
        xn = numRectangular.numerator
        print("num xn {}".format(xn))
        print("num rectangular {}".format(numRectangular))
        numerosRectangulares.append(numRectangular)

    if xn == x0:
        return 'El periodo está completo', numerosRectangulares
    else:
        return 'El periodo está incompleto',[]

def obtenerValoresIniciales():
    x0 = int(input('Valor de x0 :'))
    a  = int(input('Valor de a :'))
    m  = int(input('Valor de m :'))
    return x0,a,m

x0,a,m = obtenerValoresIniciales()
periodo, numeros = numRectMultiplicativos(x0,a,m)

print(periodo)
print(numeros)