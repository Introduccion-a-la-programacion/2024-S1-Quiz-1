# 2022-S2 Quiz 1

## Instrucciones Generales
- El archivo **debe** llamarse **Quiz1.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**,  **Entrada**, **Salida** y **Restricciones**
- Debe crear el **pseudocódigo en Pseint** y guardar el archivo en este repositorio

## tieneDigitosImpares(num)  (10 puntos)
- Construir una función que **TRUE** si los dígitos del número todos son **impares**.
- Retornará **TRUE** en el caso que todos sean impares, **FALSE** en el caso de que no.
- El parámetro **num** debe ser entero y mayor a CERO
- 
```python
>>>tieneDigitosImpares(135)     
True

>>>tieneDigitosImpares(211)     
False

>>>tieneDigitosImpares('2345')     
'Error: Tipo de parámetro es incorrecto'
```

## factorialPorRango(inicio, fin, rango)  (15 puntos)

- Desarrollar la función factorialPorRango donde realizará el factorial desde **inicio** hasta el número **fin** especificado en el parámetro de entrada
- El parámetro **rango** será la forma de cómo será el factorial, es decir de 2 en 2, o 3 en 3
- Ambos parámetros debe ser enteros positivos


```python
>>> factorialPorRango(6, 20, 4)  #6 * 10 * 14 * 18
15120

>>> factorialPorRango(2, 5, 1)  #2 * 3 * 4 * 5
120

>>> factorialPorRango('2', 5, 2)     
'Error: Parámetro num es incorrecto'
```
