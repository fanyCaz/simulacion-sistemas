from fractions import Fraction

def numRectMixto(x0:int,a:int,c:int,m:int):
    #(axn + c) /m
    xn  :int = x0
    numRectangular :int = 0
    numerosRectangulares = []
    #Formula ax0 mod m
    for i in range(m):
        fraccion = Fraction((a*xn + c) / m).limit_denominator(m)
        z = fraccion.numerator
        while(z > fraccion.denominator):
            z -= fraccion.denominator
        numRectangular = Fraction(z,fraccion.denominator)
        xn = numRectangular.numerator
        numerosRectangulares.append(xn)
    if xn == x0:
        return 'El periodo está completo', numerosRectangulares
    return 'El periodo está incompleto',[]

def obtenerValoresIniciales():
    x0 = int(input('Valor de x0 :'))
    a  = int(input('Valor de a :'))
    c  = int(input('Valor de c :'))
    m  = int(input('Valor de m :'))
    return x0,a,c,m