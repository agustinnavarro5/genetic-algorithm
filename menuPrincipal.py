from algoritmoGenetico import algoritmoGenetico
from generarPoblacion import generarPoblacion
from generarImagenes import generarImagenes
from generarDatosPoblacion import generarDatosElementos
from algoritmoSeleccion import SUS
from algoritmoCruzamiento import crossover
from algoritmoMutacion import mutacion
from fitness import fitness
import globales

#Menu de Opciones
print("Selecciona una opción: ")
print("\t1 - Proyecto con implementación de algoritmo de mutación impaciente")
print("\t2 - Proyecto con implementación de algoritmo de mutación de radio")
opcionMenu = input("inserta un numero valor >> ")
#Opción seleccionada
if opcionMenu=="1":
    globales.algoritmoSeleccionado = 1
elif opcionMenu=="2":
    globales.algoritmoSeleccionado = 2
else:
    print ("")
    input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


#Poblacion
poblacion = generarPoblacion()
#Generación de población de imágenes
imagenes = generarImagenes(poblacion)
#Fitness y datos relativos a cada imagen
datosPoblacion = generarDatosElementos(imagenes,fitness)
#Estructura de Algoritmo Genético
algoritmoGenetico(poblacion, datosPoblacion, fitness, imagenes,globales.cantidadGeneraciones,globales.tamañoPoblacion,globales.tamañoElite,globales.porcentajeMutacion, SUS,crossover,mutacion)
