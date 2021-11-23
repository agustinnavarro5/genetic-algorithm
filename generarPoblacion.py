# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:44:38 2020

@author: usuario
"""
import globales
import numpy as np
def generarIndividuo():
  individuo = []
  i = 0 
  j = i
  while i<globales.nroVariables:
    if j>5:
        j=0
    if globales.tiposDatos[j] == 1 :
            valorMinimo = globales.listaLimiteInferior[j]
            valorMaximo = globales.listaLimiteSuperior[j]
            valor = np.random.randint(valorMinimo, valorMaximo)
    else:
            valor = np.random.uniform()
    individuo.append(valor)
    i+=1
    j+=1
  return individuo

def generarPoblacion():
  poblacion = []
  i = 0 
  while i<globales.tamañoPoblacion:
    individuo =  generarIndividuo()
    poblacion.append(individuo)
    i+=1
  return poblacion
