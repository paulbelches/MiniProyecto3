from math import *
import numpy as np

def generarTiempo(t, l): 
    while True:
        t = t - (np.log(np.random.uniform())/l)
        if np.random.uniform() <= np.random.poisson(t)/l:
            return t

def simulation(serverNumber, request):
    LAMBDA = 40 # Quien llega
    T = 3600
    t = Na = Nd = 0 #t es por donde vamos
    D = []
    A = []
    td = [] #departure
    ta = []
    n = []
    pri = False
    def smaller(arrayValues, arrayCounter ):
        pos, value = 0, inf
        for i in range(serverNumber):
            if (arrayValues[i] < value and arrayCounter[i] != 0):
                value = arrayValues[i]
                pos = i
        return pos

    for i in range(serverNumber):
        D.append([])
        A.append([])
        n.append(0)
        ta.append(0)
        td.append(inf)
    flag = True
    while (flag):
        posTa = ta.index(min(ta))
        posTd = td.index(min(td))
        if (ta[posTa] <= td[posTd] and ta[posTa] <= T): # La siguiente operacion que atendemos es una llegada
            #Move pointer
            t = ta[ta.index(max(ta))] #Último tiempo de llegada
            #Counters
            Na+=1
            n[posTa]+= 1
            #Generate next
            ta[posTa] = generarTiempo(t, LAMBDA)
            if (n[posTa] == 1):
                td[posTa] = t + np.random.exponential(1/request)
            A[posTa].append(t) #Tiempo de llegada de la solicitud
        elif (td[posTd] <= ta[posTa] and td[posTd] <= T): #Attending exit case
            #Move pointer
            t = td[posTd]
            #Counters
            Nd+=1
            n[posTd]-=1
            #Last element in list
            if (n[posTd] == 0):
                td[posTd] = inf
            else:
                td[posTd] = t + np.random.exponential(1/request)
            #print(t, td, ta)
            D[posTd].append(t) #Tiempo de salida de la solicitud
        elif (min(ta[posTa],td[posTd]) > T and sum(n) > 0):
            pos = smaller(td, n)
            pri = True
            t = td[pos]
            Nd+=1
            n[pos]-=1
            if (n[pos] > 0):
                td[pos] = t + np.random.exponential(1/request)
            D[pos].append(t)#Tiempo de salida de la solicitud
        elif (min(ta[posTa], td[posTd]) > T and sum(n) == 0): 
            Tp = max(t - T, 0)
            flag = False
    return A, D

ServerAmount= 10
A,D = simulation(ServerAmount,10)
#print(len(A))
total = 0
"""
for i in range(len(A)):
    print(A[i][0],A[i][-1], len(A[i]))
    total+= len(A[i])
print("total", total)
total = 0
print("El otro")
for i in range(len(D)):
    print(D[i][0],D[i][-1], len(D[i]))
    total+= len(A[i])
print("total", total)
"""
#print(D[1][0],D[1][-1])
#print(D[0],D[-1])
"""
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
"""
"""
for i in range(ServerAmount):
    canti,ocup,libre,cola,espprom,colasec,us=info(A[i],D[i])
    print("El servidor de Gorilla Megacomputing atendio ",canti, " solicitudes, paso ocupado ",ocup," segundos y desocupado ",libre," segundos. \n Las solicitudes estuvieron en total ",cola, " segundos en cola, lo cual nos da un promedio de ",espprom, " segundos por solicitud. \n Cada segundo hubo ",colasec," solicitudes en cola.\n El momento de salida de la ultima solicitud fue en el segundo: ",us)    
"""
