from math import *
import numpy as np

def generarTiempo(t, l): 
    t = t - (np.log(np.random.uniform())/l)
    return t

def simulation(serverNumber, request, LAMBDA):
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
                td[posTa] = t - (1/request)*np.log(np.random.uniform())
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
                td[posTd] = t - (1/request)*np.log(np.random.uniform())
            #print(t, td, ta)
            D[posTd].append(t) #Tiempo de salida de la solicitud
        elif (min(ta[posTa],td[posTd]) > T and sum(n) > 0):
            pos = smaller(td, n)
            pri = True
            t = td[pos]
            Nd+=1
            n[pos]-=1
            if (n[pos] > 0):
                td[pos] = t - (1/request)*np.log(np.random.uniform())
            D[pos].append(t)#Tiempo de salida de la solicitud
        elif (min(ta[posTa], td[posTd]) > T and sum(n) == 0): 
            Tp = max(t - T, 0)
            flag = False
    return A, D

def info(listArrival,listDeparture,val=True):
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
    if (val==True):
        colasec=1/espprom 
    else: 
        colasec=0
    return canti,ocup,libre,cola,espprom,colasec,us


def cantidadNecesaria(LAMBDA, potencia):  
    flag=True
    cont=1
    while(flag==True):
        A,D = simulation(cont,potencia,LAMBDA)
        for i in range(cont):
            canti,ocup,libre,cola,espprom,colasec,us=info(A[i],D[i],False)
            #print(espprom)
            if(round(espprom,3)==0):
                flag=False
                cantidad=len(A)
            else:
                cont+=1
    print("Para manejar ",str(LAMBDA*60)," solicitudes por minuto y que siempre haya un servidor de Ant Smart Computing disponible, se necesitan alquilar ", cantidad, " servidores")

def solicitudesNecesaria(LAMBDA, factor, vi):
    cont = vi 
    flag=True
    while(flag):
        A,D = simulation(1,cont * factor,LAMBDA)
        canti,ocup,libre,cola,espprom,colasec,us=info(A[0],D[0])
        if(round(espprom,3)==0):
            flag=False
            cantidad=cont * factor
        else:
            cont+=1
    print("Para manejar ",str(LAMBDA*60)," solicitudes por minuto y que el servidor de Gorilla Megaomputing Computing este siempre disponible, se necesitan alquilar un servidor que resuelva ", cantidad, " solicitudes por segundo")

#Task 1   
print("------------------------------------Task 1------------------------------------")
ServerAmount= 10
LAMBDA=40
A,D = simulation(ServerAmount,10,LAMBDA)
Ag,Dg= simulation(1,100,LAMBDA)

canti,ocup,libre,cola,espprom,colasec,us=info(Ag[0],Dg[0])
print("El servidor de Gorilla Megaomputing atendio ",canti, " solicitudes, paso ocupado ",ocup," segundos y desocupado ",libre," segundos. \n Las solicitudes estuvieron en total ",cola, " segundos en cola, lo cual nos da un promedio de ",espprom, " segundos por solicitud. \n Cada segundo en promedio hubo ",colasec," solicitudes en cola.\n El momento de salida de la ultima solicitud fue en el segundo: ",us)   

for i in range(ServerAmount):
    canti,ocup,libre,cola,espprom,colasec,us=info(A[i],D[i])
    print("El servidor ", str(i+1), " de Ants Smart Computing atendio ",canti, " solicitudes, paso ocupado ",ocup," segundos y desocupado ",libre," segundos. \n Las solicitudes estuvieron en total ",cola, " segundos en cola, lo cual nos da un promedio de ",espprom, " segundos por solicitud. \n Cada segundo en promedio hubo ",colasec," solicitudes en cola.\n El momento de salida de la ultima solicitud fue en el segundo: ",us)   

#Task 2
print("------------------------------------Task 2------------------------------------")
cantidadNecesaria(LAMBDA, 10)
cantidadNecesaria(LAMBDA, 100)
solicitudesNecesaria(LAMBDA, 10000, 45)
#Task 3   
print("------------------------------------Task 3------------------------------------")
ServerAmount= 10
LAMBDA=100
A,D = simulation(ServerAmount,10,LAMBDA)
Ag,Dg= simulation(1,100,LAMBDA)

canti,ocup,libre,cola,espprom,colasec,us=info(Ag[0],Dg[0])
print("El servidor de Gorilla Megaomputing atendio ",canti, " solicitudes, paso ocupado ",ocup," segundos y desocupado ",libre," segundos. \n Las solicitudes estuvieron en total ",cola, " segundos en cola, lo cual nos da un promedio de ",espprom, " segundos por solicitud. \n Cada segundo en promedio hubo ",colasec," solicitudes en cola.\n El momento de salida de la ultima solicitud fue en el segundo: ",us)   

for i in range(ServerAmount):
    canti,ocup,libre,cola,espprom,colasec,us=info(A[i],D[i])
    print("El servidor ", str(i+1), " de Ants Smart Computing atendio ",canti, " solicitudes, paso ocupado ",ocup," segundos y desocupado ",libre," segundos. \n Las solicitudes estuvieron en total ",cola, " segundos en cola, lo cual nos da un promedio de ",espprom, " segundos por solicitud. \n Cada segundo en promedio hubo ",colasec," solicitudes en cola.\n El momento de salida de la ultima solicitud fue en el segundo: ",us)   

#Task 4
print("------------------------------------Task 4------------------------------------")
cantidadNecesaria(LAMBDA, 10)
cantidadNecesaria(LAMBDA, 100)
solicitudesNecesaria(LAMBDA, 100000, 10)