from math import *
import numpy as np

LAMBDA = 40 # Quien llega

def generarTiempo(t, l): # los eventos serán solamente procesos de poisson no homogeneos, así que se programa solo para eso 
    while True:
        t = t - (np.log(np.random.uniform())/l)
        if np.random.uniform() <= np.random.poisson(t)/l:
            return t

T = 3600
t = Na = Nd = n = 0 #t es por donde vamos
ta = generarTiempo(0, LAMBDA) #arrival
td = inf #departure
D = []
A = []
flag = True
while (flag):
    #print(ta, td, ta <= td, td <= ta, n)
    if (ta <= td and ta <= T): # La siguiente operacion que atendemos es una llegada
        #Move pointer
        t = ta
        #Counters
        Na+=1
        n+=1
        #Generate next
        ta = generarTiempo(t, LAMBDA)
        if (n == 1):
            td = t + np.random.exponential(1/100)
        A.append(t) #Tiempo de llegada de la solicitud
    if (td <= ta and td <= T): #Attending exit case
        #Move pointer
        t = td
        #Counters
        Nd+=1
        n-=1
        #Last element in list
        if (n == 0):
            td = inf
        else:
            td = t + np.random.exponential(1/100)
        #print(t, td, ta)
        D.append(t) #Tiempo de salida de la solicitud
    if (min(ta,td)>T and n > 0):
        #print(len(A))
        #print(len(D))
        t = td
        Nd+=1
        n-=1
        if (n > 0):
            td = t + np.random.exponential(1/100)
        D.append(t)#Tiempo de salida de la solicitud
    if (min(ta, td) > T and n == 0): 
        Tp = max(t - T, 0)
        flag = False

