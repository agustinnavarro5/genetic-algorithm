
"""
Created on Tue Dec 17 20:47:05 2019

@author: usuario
"""
import matplotlib.pyplot as plt
import numpy as np
from elite import *
from generarImagenes import generarImagenes
from generarDatosPoblacion import generarDatosElementos, ordenarPuntoCorte

def graficarMediaOMejoresFitness(array, numeroGeneraciones, titulo):
        plt.plot(np.arange(numeroGeneraciones),array,"o")
        # Añado una malla al gráfico
        plt.grid()
        plt.title(titulo)  # Colocamos el título
        plt.xticks(np.arange(numeroGeneraciones), np.arange(numeroGeneraciones), rotation = 0)  # Colocamos las etiquetas
        plt.show()
        return


def getFitnessMedia(datosPoblacion,tamañoPoblacion):
    b = 0
    for a in datosPoblacion:
        b += a[0]
    return b/tamañoPoblacion


def algoritmoGenetico(poblacion, datosPoblacion, funcion,imagenesInicial,cantidadGeneraciones,tamañoPoblacion,tamañoElite,porcentajeMutacion, algoritmoSeleccion, algoritmoCruzamiento, algoritmoMutacion):
  i=0
  arrayFitnessMedia = np.array([])
  arrayMejoresFitness = np.array([])
  individuos = np.array([])
  while i < cantidadGeneraciones:
      #Guardo el mejor individuo al comienzo para no perderlo
      datosPoblacionElite = []
      elite = getVectorElite(poblacion,datosPoblacion,datosPoblacionElite,tamañoElite)
      #Aplico algoritmo de selección
      individuos = algoritmoSeleccion(poblacion,datosPoblacion)
      #Aplico algoritmo de cruzamiento
      individuos = algoritmoCruzamiento(individuos)
      #Aplico algoritmo de mutación
      individuos = algoritmoMutacion(individuos,porcentajeMutacion)
      #Una vez obtenida la nueva población, actualizo las nuevas imágenes (población)
      imagenes = generarImagenes(individuos)
      datosPoblacion = generarDatosElementos(imagenes, funcion)
      #Asigno el Elite que alamcené al principio y lo reemplazo por el peor que obtuve
      individuos = asignarElite(individuos,elite,imagenesInicial,imagenes,datosPoblacionElite,datosPoblacion)
      #Se ordena Datos poblacion
      datosPoblacion = np.sort(datosPoblacion, order='fitness')
      datosPoblacion = list(reversed(datosPoblacion))
      datosPoblacion = ordenarPuntoCorte(datosPoblacion)
      #Obtengo el mejor individuo para graficar
      posicionMejorImagen = datosPoblacion[0][4]
      img = imagenes[posicionMejorImagen]
      #Grafico el mejor individuo de la generación
      plt.imshow(img,vmin=0,vmax=1)
      plt.show() 
      #Reemplazo población nueva por la población mejorada
      poblacion= individuos.copy()
      imagenesInicial= imagenes.copy()
      #Agrego la media de fitness de la generación para posterior gráfica
      fitnessMedia = getFitnessMedia(datosPoblacion,tamañoPoblacion)
      arrayFitnessMedia = np.append(arrayFitnessMedia,fitnessMedia)
      #Agrego el mejor valor de fitness de la generación para posterior gráfica
      mejorFitness = datosPoblacion[0][0].copy()
      arrayMejoresFitness = np.append(arrayMejoresFitness,mejorFitness)
      #Muestro ciertos parámetros informativos por generación
      print("Mejor fitness de poblacion: ",mejorFitness)
      print("Fin de generación ", i+1,". ---------------")
      i+=1
  print("Media de valores fitness: ",arrayFitnessMedia)
  print("Mejores valores fitness: ",arrayMejoresFitness)
  graficarMediaOMejoresFitness(arrayMejoresFitness,cantidadGeneraciones,'Mejores Fitness de cada generación')
  graficarMediaOMejoresFitness(arrayFitnessMedia,cantidadGeneraciones,'Media de fitness de cada generación')


