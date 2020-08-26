import pytest 
import config as cf

from Lib.ADT import list as lt
from App.View import app 


def test_loadMovies ():
    lst = app.loadMovies ()
    assert lt.size (lst) == 2000




