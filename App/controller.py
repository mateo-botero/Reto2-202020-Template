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

import config as cf
from App import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def cargar_peliculas():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    listado = loadCSVFile("SmallMoviesDetailsCleaned.csv",comparacionid)
    print("Datos cargados, " + str(lt.size(listado)) + " elementos cargados")
    return listado



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadCSVFile (file,comparacionid):
    catalogo=lt.newList(comparacionid)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(  cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for pelicula in row: 
                model.addLast(catalogo,pelicula)
    except:
        print("Hubo un error con la carga del archivo")

def tamañopeliculas(catalogo):
    return model.tamañopeliculas(catalogo)

def primera_pelicula(catalogo):
    return model.primera_pelicula(catalogo)

def ultima_pelicula(catalogo):
    return model.ultima_pelicula(catalogo)

def comparacionid (recordA, recordB):
    return model.comparacionid(recordA,recordB)
