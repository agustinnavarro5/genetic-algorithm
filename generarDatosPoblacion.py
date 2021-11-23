# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:46:48 2020

@author: usuario
"""
import numpy as np
import globales

def getVectorAjustePoblacion(vectorFitnessPoblacion,minimo,epsilum):
  ajuste = []
  for a in vectorFitnessPoblacion:
    valorAjuste = a - minimo + epsilum
    ajuste.append(valorAjuste)
  return ajuste


def ordenarPuntoCorte(array):
    prob = 0
    for a in array:
        prob += a[2]
        a[3] = prob
    return array

def fitnessPoblacion(imagenes,funcion):
    return [funcion(img) for img in imagenes]

def generarDatosElementos(imagenes,funcion):
  dtype = [('fitness', float), ('fitnessAjuste', float), ('probabilidad', float), ('puntoCorte', float),('posicionSolucion', int)]
  i=0
  puntoCorte = 0
  vectorFitnessPoblacion = fitnessPoblacion(imagenes,funcion)
  minimo = min(vectorFitnessPoblacion)
  vectorT=getVectorAjustePoblacion(vectorFitnessPoblacion,minimo,globales.epsilum)
  T = sum(vectorT)
  valores = []
  while i<globales.tamañoPoblacion:
    #Fitness
    fit = vectorFitnessPoblacion[i]
    #Ajuste de Fitness
    ajuste = vectorT[i]
    #Probabilidad de ocurrencia de Solucion
    prob = ajuste/T
    #Punto de Corte
    puntoCorte+=prob
    #Tupla de valores
    valores.append((fit,ajuste,prob,puntoCorte,i))
    i+=1
  a = np.array(valores, dtype=dtype)       # create a structured array
  a = np.sort(a, order='fitness')
  a = list(reversed(a))
  a = ordenarPuntoCorte(a)
  return a   

