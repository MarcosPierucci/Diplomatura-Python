#Ejercicio 1 

"""Cree un programa que tome tres valores por consola multiplique el primero por el segundo
y le sume el tercero. Presente el resultado en la terminal del editor"""

valor_1 = input("Ingrese un valor: ")
valor_2 = input("Ingrese un valor: ")
valor_3 = input("Ingrese un valor: ")

valor_1 = int(valor_1)
valor_2 = int(valor_2)
valor_3 = int(valor_3)

valor_aux = valor_1*valor_2

valor_final = valor_aux + valor_3

print("Primer valor ingresado: ", valor_1)
print("Segundo valor ingresado: ", valor_2)
print("Tercer valor ingresado: ", valor_3)
print(valor_1 , "Multiplicado por ", valor_2 , "Y sumado ", valor_3, "Da como resultado: " , valor_final)


#Ejercicio 2 (Este queda comentado para que se pueda correr desde el VS el resto del código)

"""Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos"""

"""import sys

#python ejercicios_unidad1.py 10 20 30

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

variable_1 = int(sys.argv[1])
variable_2 = int(sys.argv[2])
variable_3 = int(sys.argv[3])

print("Si es true es par, sino es impar")
print(variable_1 % 2 == 0)
print(variable_2 % 2 == 0)
print(variable_3 % 2 == 0)
"""

#Ejercicio 3

"""Escriba un programa que solicite el  radio de una circunferencia y permita calcular el 
perimetro. Presente el resultado en la terminal del editor"""

radio = input("Ingrese el radio de la circunferencia: ")

radio = float(radio)

longitud = 2 * 3.1416 * radio

print("La longitud de la circunferencia es: ", longitud)

#Ejercicio 4

"""Escriba un programa que solicite el radio de una circunferencia y permita calcular el
área. Presente el resultado en la terminal del editor"""

radio2 = input("Ingrese el radio de la circunferencia: ")
radio2 = float(radio2)

area = 3.1416 * radio2**2
print("El area de la circunferencia es: ", area)


#Ejercicio 5

"""Escriba un programa que solicite un valor entero por pantalla y presente en la terminal
editor el valor incrementado en un 10%"""

valor_normal = input("Ingrese un valor: ")
valor_normal = float(valor_normal)

valor_aumentado = valor_normal * 1.1
valor_aumentado = float(valor_aumentado)
print("Valor aumentado 10%: ", valor_aumentado)