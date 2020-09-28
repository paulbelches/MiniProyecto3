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

def info(listArrival,listDeparture):
    canti=len(listArrival)
    ocup=0
    for i in range(canti):
        ocup=ocup+listDeparture[i]-listArrival[i]
    us=listDeparture[(canti-1)]
    libre=0
    cola=0
    for j in range(canti-1):
        if (listDeparture[j]>listArrival[j+1]):
            dif=listDeparture[j]-listArrival[j+1]
            cola=cola+dif
        elif (listDeparture[j]<listArrival[j+1]):
            dif=listArrival[j+1]-listDeparture[j]
            libre=libre+dif
    espprom=cola/canti
    colasec=1/espprom
    return canti,ocup,libre,cola,espprom,colasec,us


canti,ocup,libre,cola,espprom,colasec,us=info(A,D)
print("El servidor de Gorilla Megacomputing atendio ",canti, " solicitudes, paso ocupado ",ocup," segundos y desocupado ",libre," segundos. \n Las solicitudes estuvieron en total ",cola, " segundos en cola, lo cual nos da un promedio de ",espprom, " segundos por solicitud. \n Cada segundo hubo ",colasec," solicitudes en cola.\n El momento de salida de la ultima solicitud fue en el segundo: ",us)    


