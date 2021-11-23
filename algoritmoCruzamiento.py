# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:08:38 2020

@author: usuario
"""
import random
import numpy as np
import globales
#Algoritmo de cruzamiento Uniform 
def getMascaraBinaria(nroVariables):
    mascara = []
    i=0
    while i<nroVariables:
        unoCero = [1, 0]
        valor = random.choice(unoCero)
        mascara.append(valor)
        i+=1
    return mascara
def uniformCrossover(padreUno,padreDos):
                #Uniform Crossover
                vectorMascaraBinaria = getMascaraBinaria(globales.nroVariables)
                j=0
                valoresHijoUno = []
                valoresHijoDos = []
                while j<len(vectorMascaraBinaria):
                    if vectorMascaraBinaria[j] == 0:
                        valoresHijoUno.append(padreUno[j])
                        valoresHijoDos.append(padreDos[j])
                    else:
                        valoresHijoUno.append(padreDos[j])
                        valoresHijoDos.append(padreUno[j])
                    j+=1
                return [valoresHijoUno,valoresHijoDos]

def crossover(individuos):
    individuosCruzados = []
    cantidadIndividuosCruzados = 0
    while cantidadIndividuosCruzados < len(individuos):
          #Si un individuo queda sin cruzar, se lo agrega automaticamente a la población
          if (len(individuos)-cantidadIndividuosCruzados) == 1:
            individuosCruzados.append(individuos[cantidadIndividuosCruzados])
            cantidadIndividuosCruzados+=1
          else:
            posicionUno = np.random.randint(0,len(individuos))
            posicionDos = np.random.randint(0,len(individuos))
            #Los individuos que al principio son los padres, luego representan los hijos(la misma variable)
            individuoUno = individuos[posicionUno].copy()
            individuoDos = individuos[posicionDos].copy()
            #Si los padres tienen las mismas características, se los agrega a ambos
            if posicionUno==posicionDos:
                 individuosCruzados.append(individuoUno)
                 individuosCruzados.append(individuoDos)
            else:
                hijos = uniformCrossover(individuoUno,individuoDos)
                individuosCruzados.append(hijos[0])
                individuosCruzados.append(hijos[1])
            cantidadIndividuosCruzados+=2
    return individuosCruzados