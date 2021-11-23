# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:28:51 2020

@author: usuario
"""
import matplotlib.image as mpimg
#Variables globales
#Lectura de imagen y dimensiones
imgGlobos = mpimg.imread('globos2.png')
imagenR = imgGlobos[:,:,0]
imagenG = imgGlobos[:,:,1]
imagenB = imgGlobos[:,:,2]
#Seleccion de algoritmo de mutacion
algoritmoSeleccionado = 0
#Dimensiones
N = len(imgGlobos)
M = len(imgGlobos[0])
#Parametros Principales
cantidadCirculos = 50
cantidadGeneraciones = 5000
tamañoPoblacion = 50
porcentajeMutacion = 0.3
tamañoElite = 2
epsilum = 0.1
#Variables: Posicion X de círculo, Posicion Y, Radio, Valor de Canal R, G y B.
nroVariables = 6*cantidadCirculos
listaLimiteInferior = [1,1,1,0,0,0]
listaLimiteSuperior = [N-1,M-1,max(N,M)/4,1,1,1]
#Indica si el valor de la variable es entera(1) o real(0)
tiposDatos = [1,1,1,0,0,0]