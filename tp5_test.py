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

def test_maxmen():
    assert list_max_men([1,2,3,4,5,6,-34,7,8],"a") == 8
    assert list_max_men([1,2,3,4,5,6,-34,7,8],"b") == -34


def test_pasword():
    assert login("usuario1", "asdasd", 0, True) == (False, 0 )
    assert login("usuario1", "asdas", 0, True) == (True, 1 )

def test_discount():
    assert dicount_cart({"producto1": {"precio": 100, "descuento": 10}, "producto2": {"precio": 50, "descuento": 5}, "producto3": {"precio": 200, "descuento": 15}}) == 307.5

def teste_dicword():
    assert frase("jose manuel") == {"jose": {4}, "manuel": {6}}
    assert frase("ramiro ferrari") == {"ramiro": {6}, "ferrari": {7}}

def test_factorial():
    assert calculate_factorial(5)==120
    assert calculate_factorial(3)==6
    assert calculate_factorial(6)==720

def test_calfigit():
    assert calculate_frequency(190,9)==1
    assert calculate_frequency(192,2)==1
    assert calculate_frequency(333,3)==3