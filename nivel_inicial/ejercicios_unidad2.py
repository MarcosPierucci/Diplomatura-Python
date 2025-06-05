def lineas_separadoras():
    print("---" * 20)

#Ejercicio 1
#Este ejercicio queda comentado para poder ejecutar el resto del codigo sin problemas

"""Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos. Utilice la estructura if/else (Este es el ejercicio 2 de la unidad 1 pero implementando if/else)"""

"""import sys

#  python ejercicios_unidad1.py 10 23 30

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

variable_1 = int(sys.argv[1])
variable_2 = int(sys.argv[2])
variable_3 = int(sys.argv[3])

if variable_1 % 2 == 0:
    print("Es par")
else: 
    print("Es impar")

if variable_2 % 2 == 0:
    print("Es par")
else: 
    print("Es impar")

if variable_3 % 2 == 0:
    print("Es par")
else: 
    print("Es impar")
"""

lineas_separadoras()

#Ejercicio 2

"""Cree una lista de frutas de 2 elementos, y realice un programa que muestre una oración
conteniendo los dos elementos de la lista concatenándolos con texto para formar una
oración con sentido. Presente el resultado en la terminal del editor"""

lista_frutas = ["peras", "manzanas"]

print("Me gustan mucho las" , lista_frutas[0], "pero las" , lista_frutas[1], "me parecen mas ricas")


lineas_separadoras()

#Ejercicio 3

"""Tome dos valores por consola, y guarde en una lista
[primer_valor, segundo_valor, la_suma_de_los_valores]
Presente el resultado en la terminal del editor"""

primer_valor = int(input("Ingrese el primer numero: "))
segundo_valor = int(input("Ingrese el segundo numero: "))



suma_de_los_valores = primer_valor + segundo_valor

lista= [primer_valor, segundo_valor, suma_de_los_valores]

print(lista)


lineas_separadoras()

#Ejercicio 4

"""Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
fecha de jubilación, presente en la terminal el mensaje “Ya está en edad de jubilarse” en 
caso contrario que presente “Aún está en edad de trabajar” """

edad = int(input("Ingrese su edad: "))

if edad >= 65:
    print("Ya está en edad de jubilarse")
else:
    print("Aún está en edad de trabajar")


lineas_separadoras()

#Ejercicio 5

"""Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una
función, de forma que la operación  se realice dentro de la misma. 
Presente el resultado en la terminal del editor"""

def calcular_longitud(radio):
    longitud = 2 * 3.1416 * radio
    return longitud

def calcular_area(radio):
    area = 3.1416 * radio2**2
    return area

def aumentar_10_porciento (valor):
    valor_aumentado = int(valor * 1.1)
    print("El valor aumentado un 10% da: " , valor_aumentado)

radio = float(input("Ingrese el radio de la circunferencia: "))
longitud = calcular_longitud(radio)
print("La longitud es: ", longitud)



radio2 = float(input("Ingrese el radio de la circunferencia: "))
area = calcular_area(radio2)
print("El area es: ", area)


valor_normal = int(input("Ingrese un valor: "))
aumentar_10_porciento(valor_normal)
