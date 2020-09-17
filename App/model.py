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
import config
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def nuevocatalogo(comparacionid):
    lst=lt.newList("ARRAY_LIST", comparacionid)
    return lst


# Funciones para agregar informacion al catalogo

def addLast(catalogo,pelicula):
    lt.addLast(catalogo,pelicula)

# ==============================
# Funciones de consulta
# ==============================

def tamañopeliculas(catalogo):
    return lt.size(catalogo)

def primera_pelicula(catalogo):
    return lt.firstElement(catalogo)

def ultima_pelicula(catalogo):
    return lt.lastElement(catalogo)

# ==============================
# Funciones de Comparacion
# ==============================

def comparacionid (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1

