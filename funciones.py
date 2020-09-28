from math import *
import numpy as np

def generarTiempo(t, l): # los eventos serán solamente procesos de poisson no homogeneos, así que se programa solo para eso 
    while True:
        t = t - (np.log(np.random.uniform())/l)
        if np.random.uniform() <= np.random.poisson(t)/l:
            return t
def simulation(serverNumber, request):
    
    def smaller(array):
        pos, value = 0, inf
        for i in range(serverNumber):
            if (array[i] < value):
                value = array[i]
                pos = i
        return pos

    LAMBDA = 40 # Quien llega
    T = 600
    t = Na = Nd = 0 #t es por donde vamos
    ta = generarTiempo(0, LAMBDA) #arrival
    td = inf #departure
    D = []
    A = []
    td = [] #departure
    ta = []
    n = []
    for i in range(serverNumber):
        D.append([])
        A.append([])
        n.append(0)
        ta.append(generarTiempo(0, LAMBDA))
        td.append(inf)
    flag = True
    while (flag):
        posTa = smaller(ta)
        posTd = smaller(td)
        if (ta[posTa] <= td[posTd] and ta[posTa] <= T): # La siguiente operacion que atendemos es una llegada
            print(ta, td, posTa, posTd, n, t)
            print("Entre 1")
            #Move pointer
            t = ta[posTa]
            #Counters
            Na+=1
            n[posTa]+= 1
            #Generate next
            ta[posTa] = generarTiempo(t, LAMBDA)
            if (n[posTa] == 1):
                td[posTa] = t + np.random.exponential(1/request)
            A[posTa].append(t) #Tiempo de llegada de la solicitud
        if (td[posTd] <= ta[posTa] and td[posTd] <= T): #Attending exit case
            print(ta, td, posTa, posTd, n)
            print("Entre 2")
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
        if (min(ta[posTa],td[posTd])>T and n[posTa if ta[posTa] < td[posTd] else posTd] > 0):
            print(ta, td, posTa, posTd, n)
            print("Entre 3")
            #print(len(A))
            #print(len(D))
            t = td[posTa if ta[posTa] < td[posTd] else posTd]
            Nd+=1
            n[posTa if ta[posTa] < td[posTd] else posTd]-=1
            if (n[posTa if ta[posTa] < td[posTd] else posTd] > 0):
                td[posTa if ta[posTa] < td[posTd] else posTd] = t + np.random.exponential(1/request)
            D[posTa if ta[posTa] < td[posTd] else posTd].append(t)#Tiempo de salida de la solicitud
        if (min(ta[posTa], td[posTd]) > T and sum(n) == 0): 
            print(ta, td, posTa, posTd, n)
            print("Entre 4")
            Tp = max(t - T, 0)
            flag = False
    return A, D

A,D = simulation(1,100)

print(len(A))
for i in range(len(A)):
    print(A[i][0],A[i][-1], len(A[i]))
for i in range(len(D)):
    print(D[i][0],D[i][-1], len(D[i]))

#print(D[1][0],D[1][-1])
#print(D[0],D[-1])

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


