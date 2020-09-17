"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
import csv
from DISClib.ADT import list as lt 
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________





# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("Bienvenido")
    print("1- Cargar listado de peliculas")
    print("2- Cargar información en la lista")
    print("3- Consulta de productora")
    print("4- Consultar de director")
    print("5- Consultar de actor")
    print("6- Consultar por género")
    print("7- Consultar por país")
    print("0- Salir")



while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Cargando listado de peliculas....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.cargar_peliculas()
        print("Peliculas cargadas: "+str(controller.tamañopeliculas(cont)))
        print("Primera pelicual: ")
        print("Titulo:" +str(controller.primera_pelicula(cont)["title"]))
        print("Fecha de estreno: "+ str(controller.primera_pelicula(cont)["release_date"]))
        print("Promedio de votacion: "+str(controller.primera_pelicula(cont)["vote_average"]))
        print("Numero de votos: "+str(controller.primera_pelicula(cont)["vote_count"]))
        print("Idioma: "+str(controller.primera_pelicula(cont)["original_language"]))
        print("Ultima pelicual: ")
        print("Titulo:" +str(controller.ultima_pelicula(cont)["title"]))
        print("Fecha de estreno: "+ str(controller.ultima_pelicula(cont)["release_date"]))
        print("Promedio de votacion: "+str(controller.ultima_pelicula(cont)["vote_average"]))
        print("Numero de votos: "+str(controller.ultima_pelicula(cont)["vote_count"]))
        print("Idioma: "+str(controller.ultima_pelicula(cont)["original_language"]))


    else:
        sys.exit(0)
sys.exit(0)

    