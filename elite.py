# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:07:14 2020

@author: usuario
"""

#Elite
def asignarElite(individuos,elite,imagenesInicial,imagenes,datosPoblacionElite,datosPoblacion):
    i=0
    while i < len(elite):
        posicionEliteActual = datosPoblacionElite[i][4]
        posicionPeorIndividuo = datosPoblacion[len(individuos)-1-i][4]
        individuos[posicionPeorIndividuo] = elite[i]
        imagenes[posicionPeorIndividuo] = imagenesInicial[posicionEliteActual]
        datosPoblacionElite[i][4] = posicionPeorIndividuo
        datosPoblacion[len(individuos)-1-i] = datosPoblacionElite[i]
        i+=1
    return individuos      
def getVectorElite(poblacion,datosPoblacion,datosPoblacionElite,tamañoElite):
    i=0
    elite = []
    while i < tamañoElite:
        posicionMejorIndividuo = datosPoblacion[i][4]
        elite.append(poblacion[posicionMejorIndividuo])
        datosPoblacionElite.append(datosPoblacion[i])
        i+=1
    return elite    