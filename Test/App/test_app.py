
import pytest
import config
from DISClib.ADT import list as lt
from App import reto
assert pytest
assert config


def test_loadMovies():
    lst = reto.loadMovies()
    assert lt.size(lst) == 2000
