from math import *
from Random import *

LAMBDA = 40 # Quien llega
LAMBDA2 = 100 #Cuanto se tarda

def generarTiempo(s, l): 
    return s-(1/l) * log(random())

T = 60
t = Na = Nd = n = 0 #t es por donde vamos
ta = generarTiempo(0, LAMBDA) #arrival
td = inf #departure
D = []
A = []

if (ta <= td and ta <= T):
    t = ta
    Na+=1
    n+=1
    ta = generarTiempo(0, LAMBDA)
    if (n == 1):
        y = generarTiempo(t, LAMBDA2)
        td = t + y
    A[Na] = t #Tiempo de llegada de la solicitud
if (td <= ta and td<= T): 
    t = td
    Nd+=1
    n-=1
    if (n == 1):
        td = inf
    else:
        y = generarTiempo(t, LAMBDA2)
        td = t + y
    D[Nd] = t #Tiempo de salida de la solicitud
if (min(ta,td)>T and n > 0):
    t = td
    Nd+=1
    n-=1
    if (n > 0):
        y = generarTiempo(t, LAMBDA2)
        td = t + y
    D[Nd] = t#Tiempo de salida de la solicitud
if (min(ta, td) > T): 
    Tp = max(t - T, 0)