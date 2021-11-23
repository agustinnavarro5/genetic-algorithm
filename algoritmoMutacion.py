# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 00:09:54 2020

@author: usuario
"""

import globales
import math
import random
import numpy as np
from generarImagenes import generarImagen
from fitness import fitness
import matplotlib.pyplot as plt

#Algoritmo de mutación impaciente
def aporta(circulo):
        diferenciaR = 0
        diferenciaG = 0
        diferenciaB = 0
        contador = 0
        #radio del circulo
        r = circulo[2]
        ri1 = min(r, circulo[0]-1)
        ri2 = min(r, N - circulo[0])
        rj1 = min(r, circulo[1]-1)
        rj2 = min(r, N - circulo[1])
        j=-rj1
        while j<rj2:
            i=-ri1
            while i<ri2:
                #si el pixel esta dentro del circulo actual
                if i*i + j*j < r*r:
                    x = int(circulo[0] + i)
                    y = int(circulo[1] + j)
                    diferenciaR += abs(globales.imagenR[x,y] - circulo[3])
                    diferenciaG += abs(globales.imagenG[x,y] - circulo[4])
                    diferenciaB += abs(globales.imagenB[x,y] - circulo[5])
                    contador+=1
                i+=1
            j+=1 
        #saco el promedio de colores (de cada canal RGB)
        diferenciaR = diferenciaR/contador
        diferenciaG = diferenciaG/contador
        diferenciaB = diferenciaB/contador
        return (-diferenciaR-diferenciaG-diferenciaB)/3
    
def getCirculosAportanYNoAportan(individuo, valorMedioMutacion):
    #Parametros para circulo que más aporta
    j=0
    maximoAporte = -1
    circuloFinal = []
    circulos = []
    posicionCirculoFinal = 0
    #Parametros para almacenar los circulos que menos aportan
    cantidadCirculosNoAportan = int(valorMedioMutacion)
    valoresCirculosNoAportan = []
    circulosNoAportan = []
    posicionesCirculosNoAportan = []
    valorMinimoDelQueMenosAporta = 0
    posicionMinimoDelQueMenosAporta = 0
    while j<len(individuo):
        circulo = individuo[j:j+6]
        aporteCirculo = aporta(circulo)
        sumaTotalRGB =0
        sumaTotalRGB+= circulo[3]
        sumaTotalRGB+= circulo[4]
        sumaTotalRGB+= circulo[5]
        #Condiciones: valor de aporte entre uno establecido, radio entre tanto y tanto, y suma de RGB entre tanto y tanto
        if aporteCirculo>-0.3 and circulo[2]<=4 and circulo[2]>=2 and sumaTotalRGB<=2.6 :
            circulos.append(circulo)
            j+=6
            continue
        elif aporteCirculo > maximoAporte:
            #Si no encuentra uno que aporte de acuerdo a las condiciones, lo deja como el que más aporta
            # provisoriamente
            maximoAporte = aporteCirculo
            circuloFinal = circulo
            posicionCirculoFinal = j
        #Almaceno las posiciones de los circulos que menos aportan
        if len(valoresCirculosNoAportan) < cantidadCirculosNoAportan:
                valoresCirculosNoAportan.append(aporteCirculo)
                circulosNoAportan.append(individuo[j:j+6])
                posicionesCirculosNoAportan.append(j)
                valorMinimoDelQueMenosAporta = max(valoresCirculosNoAportan)
                posicionMinimoDelQueMenosAporta = valoresCirculosNoAportan.index(valorMinimoDelQueMenosAporta)
        else:
            if aporteCirculo < valorMinimoDelQueMenosAporta:
                circulosNoAportan[posicionMinimoDelQueMenosAporta] = individuo[j:j+6]
                posicionesCirculosNoAportan[posicionMinimoDelQueMenosAporta] = j
                valoresCirculosNoAportan[posicionMinimoDelQueMenosAporta] = aporteCirculo
                valorMinimoDelQueMenosAporta = max(valoresCirculosNoAportan)
                posicionMinimoDelQueMenosAporta = valoresCirculosNoAportan.index(valorMinimoDelQueMenosAporta)
        j+=6

    
    
    if len(circulos)==0:
        #Si no se encontró algún círculo que aporte, se retorna el que más cerca está de las condiciones establecidas
        return [[circuloFinal,True,posicionCirculoFinal],circulosNoAportan,posicionesCirculosNoAportan]
    else:
        return [circulos,circulosNoAportan,posicionesCirculosNoAportan]
    
def mutarCirculos(circuloAporta,circulosNoAportan):
    #La idea es contar lo que aportan los circulos(que no aportan y del mismo radio del que aporta) 
    #posicionados consecutivamente tomando como inicio el cìrculo(que si aporta) 
    # en orientacion hacia arriba, abajo, derecha, izquierda, y diagonales superiores e inferiores
    radio = circuloAporta[2]
    hipotenusa = int(math.sqrt((radio**2)+(radio**2)))-radio
    diametro = radio
    #Este vector contiene el aporte de cada circulo en la nueva posicion segun la orientación (cada elemento
    # corresponde a una orientacion)
    contadorAportes = [0,0,0,0,0,0,0,0]
    #Es una lista que posee los valores a incrementar en las coordenadas X y/o Y de los circulos por cada circulo a reorientar
    listaIncrementadoresCoordenadas = [[0,diametro],[0,-diametro],
                                       [diametro,0],[-diametro,0],
                                       [-hipotenusa,hipotenusa],[hipotenusa,hipotenusa],
                                       [-hipotenusa,-hipotenusa],[hipotenusa,-hipotenusa]]
    #Esta lista nos sirve para luego obtener la mejor orientación calculada
    listaIncrementadoresCoordenadasAux = listaIncrementadoresCoordenadas.copy()
    k=1
    for circulo in circulosNoAportan:
        valorMaximo = diametro*k
        valorMaximoHipotenusa = hipotenusa*k
        #Mientras no supere las dimensiones
        if valorMaximo >= N and valorMaximo>= M and valorMaximoHipotenusa>= N and  valorMaximoHipotenusa>= M:
            break
        #Inicializa el circulo que no aporta con los valores del que si aporta
        circulo[0] = circuloAporta[0]
        circulo[1] = circuloAporta[1]
        circulo[2] = circuloAporta[2]
        circulo[3] = circuloAporta[3]
        circulo[4] = circuloAporta[4]
        circulo[5] = circuloAporta[5]
        # calcula el valor de aporte del circulo en las distintas orientaciones
        for i in range(len(listaIncrementadoresCoordenadas)):
            #Verifica que el nuevo centro del cìrculo se encuentre dentro de los pixeles de la img completa
            if (circulo[0]+listaIncrementadoresCoordenadas[i][0])<N and (circulo[0]+listaIncrementadoresCoordenadas[i][0])>0 and (circulo[1]+listaIncrementadoresCoordenadas[i][1])<M and (circulo[1]+listaIncrementadoresCoordenadas[i][1])>0:
                circulo[0] += int(listaIncrementadoresCoordenadas[i][0])
                circulo[1] += int(listaIncrementadoresCoordenadas[i][1])
                contadorAportes[i] += aporta(circulo)
                # se vuelve a la posicion XY inicio para que no se acumule
                circulo[0] = circuloAporta[0]
                circulo[1] = circuloAporta[1]
            else:
                #como no se tiene en cuenta un circulo porque excede las dimensiones, se pone el menor valor posible(-1)
                contadorAportes[i] += -1
        #Incremento la posicion XY para desplazamiento del proximo circulo e ir formando la consecución de círculos superpuestos
        listaIncrementadoresCoordenadas = [[elemento[0]+int(elemento[0]/k),
                                            elemento[1]+int(elemento[1]/k)]
                                    for elemento in listaIncrementadoresCoordenadas]
        k+=1
        
    #Obtengo el mayor contador de aportes segun la orientacion para mutar los circulos que no aportan
    # en la respectiva orientaciòn    
    posicionMayor = contadorAportes.index(max(contadorAportes))
    #Obtiene las coordenadas incrementadoras según la orientación que más aporte
    coordenadasIncrementadoras = listaIncrementadoresCoordenadasAux[posicionMayor]
    k=1
    for circulo in circulosNoAportan:
        #Inicializa el circulo que no aporta con los valores del que si aporta
        circulo[0] = circuloAporta[0]
        circulo[1]= circuloAporta[1]
        circulo[2] = circuloAporta[2]
        circulo[3] = circuloAporta[3]
        circulo[4] = circuloAporta[4]
        circulo[5] = circuloAporta[5]
        #Verifica que el nuevo centro del cìrculo se encuentre dentro de los pixeles de la img completa
        if (circulo[0]+coordenadasIncrementadoras[0])<N and (circulo[0]+coordenadasIncrementadoras[0])>0 and (circulo[1]+coordenadasIncrementadoras[1])<M and (circulo[1]+coordenadasIncrementadoras[1])>0:
            circulo[0] +=  coordenadasIncrementadoras[0]
            circulo[1] += coordenadasIncrementadoras[1]
        else:
            #Aquellos circulos que superen las dimensiones, se mutarán completamente
            # y con un rango de radio pequeño
            j=0
            while j<len(circulo):
                if j == 2:
                    #asigno un radio entre 1 y 6
                    circulo[j] = np.random.randint(3, 6)
                    j+=1
                    continue
                if globales.tiposDatos[j] == 1 :
                        valorMinimo = globales.listaLimiteInferior[j]
                        valorMaximo = globales.listaLimiteSuperior[j]
                        circulo[j] = np.random.randint(valorMinimo, valorMaximo)
                else:
                        circulo[j] = np.random.uniform()
                j+=1
        #Se incrementan las posiciones XY para desplazamiento del proximo circulo a mutar
        coordenadasIncrementadoras = [resultado + int(resultado/k)
                    for resultado in coordenadasIncrementadoras]
        k+=1
    return circulosNoAportan


def mutacion(individuos,porcentajeMutacion):
       #La mutación se implementará con 2 algoritmos, por lo que el valor de mutación debe ser el medio
       valorMutacion = porcentajeMutacion*len(individuos)
       valorMedioMutacion = valorMutacion/2
       
       #Algoritmo de mutación: Uniform mutation
       i = 0
       while i < valorMedioMutacion:
           posicionSolucion = np.random.randint(0,len(individuos))
           posicionCoordenada = np.random.randint(0,globales.nroVariables)
           arribaAbajo = [1, 0]
           limiteElegido = random.choice(arribaAbajo)
           ###Defino la posicion equivalente de la coordenada en la lista de límites inferior o superior
           cociente = math.floor((posicionCoordenada+1)/6)
           posicionListaLimite= (posicionCoordenada+1) - cociente*6
           if limiteElegido == 1:
               valorMaximo= globales.listaLimiteSuperior[posicionListaLimite-1]
           else:
               valorMaximo = globales.listaLimiteInferior[posicionListaLimite-1]
           valorActual = individuos[posicionSolucion][posicionCoordenada]
           s = np.random.uniform()
           valorMutacion = s*valorActual + (1-s)*valorMaximo
           ###Verifica el tipo de dato de la coordenada
           if globales.tiposDatos[posicionListaLimite] == 1:
               valorMutacion = int(np.round(valorMutacion))
           individuoMutado = individuos[posicionSolucion].copy()
           individuoMutado[posicionCoordenada] = valorMutacion
           individuos[posicionSolucion] = individuoMutado
           i+=1
           
       i=0
       if globales.algoritmoSeleccionado==1:
           
           #Algoritmo de mutación: Mutación impaciente
           
           #Muta solo un individuo 
           posicionSolucion = np.random.randint(0,len(individuos))
           individuoMutado= individuos[posicionSolucion]
           #Obtiene un conjunto de circulos que aportan y no aportan a la imagen
           circulos = getCirculosAportanYNoAportan(individuoMutado, valorMedioMutacion)
           circulosAportan = circulos[0]
           circulosNoAportan = circulos[1]
           posicionesCirculosNoAportan = circulos[2]
           #Controlo si se encontraron circulos que aporten segun condiciones establecidas 
           # o se trata del que mejor aporta sin cumplir dichas condiciones
           if len(circulosAportan)==3 and circulosAportan[1] == True:
                   #Se elige un circulo que haya aportado lo maximo posible 
                   circuloAporta = circulosAportan[0]
                   #Se controla si el color promedio del circulo tiende a ser claro
                   sumaTotalRGB =0
                   sumaTotalRGB+= circuloAporta[3]
                   sumaTotalRGB+= circuloAporta[4]
                   sumaTotalRGB+= circuloAporta[5]
                   if sumaTotalRGB>2.6:
                        #Actualiza el circulo que aporta en otro color para que no siga
                        # cayendo en el mismo circulo que no cumple las condiciones y confunde
                        # al algoritmo con un circulo bueno
                        circuloAporta[3] = np.random.uniform()
                        circuloAporta[4] = np.random.uniform()
                        circuloAporta[5] = np.random.uniform()
                        individuoMutado[circulosAportan[2]:circulosAportan[2]+6]=circuloAporta
           else:
                   #Si se encontró al menos un círculo que aporte y cumpla con las condiciones de estos circulos, se eligirá uno aleatoriamente
                   posicionCirculoAportaOptado = np.random.randint(0, len(circulosAportan))
                   circuloAporta = circulosAportan[posicionCirculoAportaOptado]
           #Se mutan los circulos que no aportan por aquellos que estan contenidos en la linea de circulos que aportan
           circulosMutados = mutarCirculos(circuloAporta,circulosNoAportan)
           #Actualiza individuo mutado a población
           for i in range(len(posicionesCirculosNoAportan)):
               posicionCirculoNoAporta = posicionesCirculosNoAportan[i]
               individuoMutado[posicionCirculoNoAporta:posicionCirculoNoAporta+6] = circulosMutados[i]
           individuos[posicionSolucion] = individuoMutado
           #Muestra img de individuo mutado
           [imgR,imgG,imgB] = generarImagen(N,M,individuoMutado)
           img =  np.ones((N,M,3))
           img[:,:,0] = imgR;
           img[:,:,1] = imgG;
           img[:,:,2]= imgB;
           fitnessImgMutada = fitness(img)
           print("fitness img mut: ",fitnessImgMutada)
           plt.imshow(img,vmin=0,vmax=1)
           plt.show()
       else:
           #Solo muta el radio
           while i < valorMedioMutacion:
               posicionSolucion = np.random.randint(0,len(individuos))
               numeroCirculo = np.random.randint(0,globales.cantidadCirculos)
               posicionCoordenada = numeroCirculo*6 +  2
               radioNuevo = np.random.randint(globales.listaLimiteInferior[2], 5)
               individuoMutado = individuos[posicionSolucion].copy()
               individuoMutado[posicionCoordenada] = radioNuevo
               individuos[posicionSolucion] = individuoMutado
               i+=1
       return individuos

N = globales.N
M = globales.M