import pytest 
import config as cf

from DISClib.ADT import list as lt
from App import reto


def test_loadMovies ():
    lst = reto.loadMovies ()
    assert lt.size (lst) == 2000




