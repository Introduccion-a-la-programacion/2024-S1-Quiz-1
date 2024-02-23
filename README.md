# Quiz 1

## Instrucciones Generales
- El archivo **debe** llamarse **Quiz1.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**,  **Entrada**, **Salida** y **Restricciones**
- Debe crear el **pseudocódigo en Pseint** y guardar el archivo en este repositorio

## provinciaPerteneciente(digito)
- Desarrolle una función llamada **provinciaPerteneciente(digito)** y que retorne el **nombre** de la provincia según el dígito de entrada. El valor del dígito es **entero** y **no debe ser negativo** y los valores válidos para el parámetro deben ser entre 1 a 7
- Debe ser implementado usando **ELIF**
```python
>>> provinciaPerteneciente(1)
"San José"
>>> provinciaPerteneciente(2)
"Alajuela"
>>> provinciaPerteneciente(3)
"Cartago"
>>> provinciaPerteneciente(4)
"Heredia"
>>> provinciaPerteneciente(5)
"Puntarenas"
>>> provinciaPerteneciente(6)
"Guanacaste"
>>> provinciaPerteneciente(7)
"Limón"
>>> provinciaPerteneciente(10)
"Error: Valor no reconocido"

```
## sumaDigitosImpares(num)  
- Desarrolle una función llamada **sumaDigitosImpares(num)** que, dado un número **positivo** **entero**, este debe retornar la **suma** de sus dígitos si estos son **impares**.
- Ejemplo:
- Numero = 12354879
- Resultado = 25, debido a que los dígitos 1,3,5,7 y 9 son impares y la suma de ellos dos son 25

```python
>>>sumaDigitosImpares(135)     
9
>>>sumaDigitosImpares(611)     
2
>>>sumaDigitosImpares('2345')     
"Error: Tipo de parámetro es incorrecto"

>>>sumaDigitosImpares(-2345)     
"Error: El valor de num debe ser positivo"
```

## sumaDigitosImpares_v2(num)  
- Desarrolle una función llamada **sumaDigitosImpares(num)** que, dado un número **entero**, este debe retornar la **suma** de sus dígitos si estos son **impares**.
- Si el número **es negativo** el resultado debe conservar el signo
- Ejemplo:
- Numero = 12354879
- Resultado = 25, debido a que los dígitos 1,3,5,7 y 9 son impares y la suma de ellos dos son 25

```python
>>>sumaDigitosImpares_v2(135)     
9
>>>sumaDigitosImpares_v2(-611)     
-2
>>>sumaDigitosImpares_v2('2345')     
"Error: Tipo de parámetro es incorrecto"

```

