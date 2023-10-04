import pytest
from tp5Funciones import *
"""
@pytest.mark.parametrize("a, res",[
    ("44140492",True),
    ("12345678",True),
    ("441",False),
    ])
def test_dni(a, res):
    assert tamanioDni(a) == res
"""


def test_sizestring():
    assert size_string("ramiro ferrari") == 7
    assert size_string("ferrari ramiro") == 6
    assert size_string("arbol de avion") == 5

def test_partner():
    assert partner("ramiro ferrari","44140492") == ["ramiro","44140492","ramiro441"]
    assert partner("ferrari adrian","12345678") == ["ferrari","12345678","ferrari123"]
    assert partner("jose miguel","87654321") == ["jose","87654321","jose876"]
    assert partner("pochita sacaachispita","21346578") == ["pochita","21346578","pochita213"]

def test_temperatura():
    assert prom_2_temp(10,2)==6
    assert prom_2_temp(10,5)==7.5
    assert prom_2_temp(10,8)==9

def test_espacios():
    assert espacios_word("hola que tal") == "h o l a   q u e   t a l "
    assert espacios_word("chau nos vemos") == "c h a u   n o s   v e m o s "