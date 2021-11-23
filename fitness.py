# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:36:04 2020

@author: usuario
"""
import globales
def fitness(individuo):
   imgR = individuo[:,:,0]
   imgG = individuo[:,:,1]
   imgB = individuo[:,:,2]
   N = globales.N
   M = globales.M
   return -sum(sum( abs(imgR-globales.imagenR)))/(N*M)-sum(sum( abs(imgG-globales.imagenG)))/(N*M)-sum(sum( abs(imgB-globales.imagenB)))/(N*M)
