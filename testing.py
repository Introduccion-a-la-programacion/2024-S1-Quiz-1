import Quiz1;
import pytest;

def test_provinciaPerteneciente_1():
    assert Quiz1.provinciaPerteneciente(1) == "San José"

def test_provinciaPerteneciente_2():
    assert Quiz1.provinciaPerteneciente(3) == "Cartago"

def test_provinciaPerteneciente_3():
    assert Quiz1.provinciaPerteneciente(7) == "Limón"

def test_provinciaPerteneciente_4():
    assert Quiz1.provinciaPerteneciente(10) == "Error: Valor no reconocido"    
    
    
def test_sumaDigitosImpares_1():
    assert Quiz1.sumaDigitosImpares(135) == 9

def test_sumaeDigitosImpares_2():
    assert Quiz1.sumaDigitosImpares(611) == 2

def test_sumaDigitosImpares_3():
    assert Quiz1.sumaDigitosImpares('2345') == "Error: Tipo de parámetro es incorrecto" 

def test_sumaDigitosImpares_4():
    assert Quiz1.sumaDigitosImpares(-2345) == "Error: El valor de num debe ser positivo"


def test_sumaDigitosImpares_v2_1():
    assert Quiz1.sumaDigitosImpares_v2(135) == 9

def test_sumaeDigitosImpares_v2_2():
    assert Quiz1.sumaDigitosImpares_v2(611) == 2

def test_sumaDigitosImpares_v2_3():
    assert Quiz1.sumaDigitosImpares_v2('2345') == "Error: Tipo de parámetro es incorrecto" 
    
