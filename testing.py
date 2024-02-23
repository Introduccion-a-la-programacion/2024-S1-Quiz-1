import Quiz1;
import pytest;


def test_tieneDigitosImpares_1():
    assert Quiz1.tieneDigitosImpares(135) == True

def test_tieneDigitosImpares_2():
    assert Quiz1.tieneDigitosImpares(211) == False

def test_tieneDigitosImpares_3():
    assert Quiz1.tieneDigitosImpares('2345') == 'Error: Tipo de parámetro es incorrecto'    
    
    
def test_factorialPorRango_1():
    assert Quiz1.factorialPorRango(6, 20, 4) == 15120

def test_factorialPorRango_2():
    assert Quiz1.factorialPorRango(2, 5, 1) == 120

def test_factorialPorRango_5():
    assert Quiz1.factorialPorRango('2', 5, 2) == 'Error: Parámetro Inicio num es incorrecto' 
    
    
