#Movimiento browniano

#Movimiento Browniano refiere a una partícula cambiando su posición uniformemente al azar. 

from random import random
random()

def generator():
    pos = 0
    dur = 10
    mayor = 0
    pos_values = []
    for t in range(dur):
        if random() < 0.5:
            pos+=1
        else:
            pos -=1
        pos_values.append( pos )
        mayor = max(pos,mayor)

    return [pos_values,mayor]