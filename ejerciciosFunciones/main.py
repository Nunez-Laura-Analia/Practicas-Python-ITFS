# EJERCICIO 1
def promedio(valor1, valor2):
    return (valor1 + valor2)/2.0

n1 = float(input("Ingrese el valor 1:"))
n2 = float(input("Ingrese el valor 2:"))
prom = promedio(n1, n2)
print("Promedio:",prom)

# EJERCICIO 2
def es_triangulo (A, B, C):
    if (A+B)>C:
        return True
    elif (A+C)>B:
        return True
    elif (B+C)>A:
        return True
    else:
        return False

L1 = float(input("Ingrese la longitud del 1er lado: "))
L2 = float(input("Ingrese la longitud del 2do lado: "))
L3 = float(input("Ingrese la longitud del 3er lado: "))
if es_triangulo(L1, L2, L3):
    print("Se puede formar un triángulo")
else:
    print("No se puede formar un triángulo")

# EJERCICIO 3
def es_par (n1):
    if n1 % 2 == 0:
        return True
    else:
        return False
            
n1 = int(input("Ingrese un numero para saber si es par o impar "))
if es_par(n1):
    print("El numero ingresado es un numero par")
else:
    print("El numero ingresado no es un numero impar")


# EJERCICIO 4
def es_mayor (n1, n2):
    if n1 > n2:
        return n1
    else: 
        return n2

n1 = float(input("Ingrese el valor 1: "))
n2 = float(input("Ingrese el valor 2: "))
mayor = es_mayor(n1, n2)
print("El numero mayor es:",mayor)

# EJERCICIO 5
def es_menor (vector):
    numero_menor = vector[0]
    for elemento in vector:
        if elemento < numero_menor:
            numero_menor = elemento
    return numero_menor

n1 = float(input("Ingrese el valor 1:"))
n2 = float(input("Ingrese el valor 2:"))
n3 = float(input("Ingrese el valor 3:"))
vector = [n1, n2, n3]
menor = es_menor(vector)
print("El numero mayor es:",menor)

# EJERCICIO 6
def promedio (vector):
    sumaTotal = 0
    for elemento in vector:
        sumaTotal = elemento + sumaTotal
    prom = sumaTotal / len(vector) 
    return prom

n1 = float(input("Ingrese el valor 1:"))
n2 = float(input("Ingrese el valor 2:"))
n3 = float(input("Ingrese el valor 3:"))
vector = [n1, n2, n3]
prom = promedio(vector)
print("El numero mayor es:",prom)

#EJERCICIO 7
def es_primo (n1):
    if n1 <= 1:
        return False
    elif n1 == 2:
        return True
    else:
        for n in range(2, n1):
            if n1 % n == 0:
                return False
        return True
            
n1 = int(input("Ingrese un numero para saber si es primo "))
if es_primo(n1):
    print("El numero ingresado es un numero primo")
else:
    print("El numero ingresado no es un numero primo")

#EJERCICIO 8 
import random

def tirar_los_dados(cantidad_de_dados: int):
    vector = []
    for n in range(cantidad_de_dados):
        numero = int(random.randint(1, 6))
        vector.append(numero)
        
    sumaTotal = 0
    for elemento in vector:
        sumaTotal = elemento + sumaTotal
    
    return sumaTotal

cantidad_de_dados =int(input("Ingrese la cantidad de dados a tirar:"))
suma_dados = tirar_los_dados(cantidad_de_dados)
print(f"Los numeros de los dados son: {suma_dados}")