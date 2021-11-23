# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:45:41 2020

@author: usuario
"""
import numpy as np
import globales
def generarImagen(N,M,individuo):
    #Se generan vectores por cada canal de color para almacenar el aporte de cada píxel en cada canal
    ImgR = np.ones((N, M))
    ImgG = np.ones((N, M))
    ImgB = np.ones((N, M))
    #El vector Contador permitirá obtener un promedio de color en cada píxel de los vectores RGB
    Cnt = np.ones((N, M))
    k=0
    while k<len(individuo):
        #radio del circulo
        r = individuo[k+2]
        #Obtengo puntos extremos del círculo de manera de recorrer cada pixel
        # que lo compone horizontal y verticalmente
        ri1 = int(min(r, individuo[k]-1))
        ri2 = int(min(r, N - individuo[k]))
        rj1 = int(min(r, individuo[k+1]-1))
        rj2 = int(min(r, N - individuo[k+1]))
        #Se genera una lista o tupla que contiene todos los píxeles identificados de los círculos para registrar
        # el aporte de cada uno en cada canal de color
        lista = tuple([(int(individuo[k]+l),int(individuo[k+1]+h)) for l in range(-ri1,ri2) for h in range(-rj1,rj2) if (l*l + h*h)<(r*r)])
        #Recorro cada pixel
        for i in range(len(lista)):
                    #Obtengo la posición X e Y del píxel en cuestión
                    x = lista[i][0]
                    y = lista[i][1]
                    #aumento en 1 la cantidad de colores en el pixel i,j
                    Cnt[x,y] = Cnt[x,y] + 1
                    #agrego componente de color a la imagen
                    ImgR[x,y] = ImgR[x,y] + individuo[k+3]
                    ImgG[x,y] = ImgG[x,y] + individuo[k+4]
                    ImgB[x,y] = ImgB[x,y] + individuo[k+5]
        k+=6
    #saco el promedio de colores (de cada canal RGB)
    ImgR = ImgR / Cnt;
    ImgG = ImgG / Cnt;
    ImgB = ImgB / Cnt;
    return [ImgR,ImgG,ImgB]

def generarImagenes(poblacion):
    imagenes = []
    for i in poblacion:
        [imgR,imgG,imgB] = generarImagen(globales.N,globales.M,i)
        img =  np.ones((globales.N,globales.M,3))
        img[:,:,0] = imgR;
        img[:,:,1] = imgG;
        img[:,:,2]= imgB;
        imagenes.append(img)
    return imagenes

