# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:07:59 2020

@author: usuario
"""
import numpy as np
#Algoritmo de Selección: stochastic Universal Sampling
def getValorAleatorioSUS(tamañoPoblacionRestante):
    r = np.random.rand()
    p = 1/tamañoPoblacionRestante
    s = p*r
    return s

def SUS(poblacion,datosPoblacion):
    i = 0 
    individuos = []
    valorAleatorio = getValorAleatorioSUS(len(poblacion))
    while i<len(poblacion):
        p = i/len(poblacion)
        puntoActual = valorAleatorio + p
        for a in datosPoblacion:
            if puntoActual < a[3]:
                posicionSolucion = a[4]
                solucion = poblacion[posicionSolucion].copy()
                individuos.append(solucion)
                break
        i+=1
    return individuos
