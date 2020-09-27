from math import *
import numpy as np

LAMBDA = 40 # Quien llega
LAMBDA2 = 100 #Cuanto se tarda


def generarTiempo(s, l): 
    return s-(1/l) * log(np.random.rand())

T = 1
t = Na = Nd = n = 0 #t es por donde vamos
ta = generarTiempo(0, LAMBDA) #arrival
td = inf #departure
D = []
A = []
flag = True
while (flag):
    #print(t)
    if (ta <= td and ta <= T): # La siguiente operacion que atendemos es una llegada
        #Move pointer
        t = ta
        #Counters
        Na+=1
        n+=1
        #Generate next
        ta = generarTiempo(t, LAMBDA)
        if (n == 1):
            y = generarTiempo(t, LAMBDA2)
            td = t + y
        A.append(t) #Tiempo de llegada de la solicitud
    elif (td <= ta and td<= T): #Attending exit case
        #Move pointer
        t = td
        #Counters
        Nd+=1
        n-=1
        #Last element in list
        if (n == 1):
            td = inf
        else:
            y = generarTiempo(t, LAMBDA2)
            td = t + y
        #print(t, td, ta)
        D.append(t) #Tiempo de salida de la solicitud
    elif (min(ta,td)>T and n > 0):
        t = td
        Nd+=1
        n-=1
        if (n > 0):
            y = generarTiempo(t, LAMBDA2)
            td = t + y
        D.append(t)#Tiempo de salida de la solicitud
    elif (min(ta, td) > T and n == 0): 
        Tp = max(t - T, 0)
        flag = False

print(t)
print(A)
print(D)