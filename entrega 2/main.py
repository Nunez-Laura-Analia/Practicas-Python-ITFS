# EJERCICIO 1
edad = int(input("Ingrese su edad: "))
if edad > 16:
    print("La edad es:", edad)

# EJERCICIO 2
dado1 = int(input("Ingrese el valor del 1er dado:"))
dado2 = int(input("Ingrese el valor del 2do dado:"))
suma = dado2 + dado1
if suma > 7:
    print("La suma es mayor a 7")
else:
    print("La suma es menor a 7")

# EJERCICIO 3
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Disculpe, debe ser mayor de 18 años")

# EJERCICIO 4
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Disculpe, debe ser mayor de 18 años.")
else:
    nombreApellido = input("Ingrese su nombre y apellido: ")

# EJERCICIO 5
edad = int(input("Ingrese su edad: "))
if (edad < 16):
    print("Disculpe, debe ser mayor de 18 años")
elif edad == 16 or edad == 17:
    adultoResponsable = input("Ingrese el nombre de un adulto responsable: ")
else:
    nombre = input("Ingrese su nombre: ")

# EJERCICIO 6
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad > 16 :
    print("Bienvenido/a:", nombre)
else:
    print("Disculpe, debe ser mayor de 16 años")

# EJERCICIO 7
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercero numero: "))
promedio = (numero1 + numero2 + numero3) / 3

if promedio < 4:
    print("Usted desaprobo la materia.")
elif promedio >= 4 and promedio < 7 :
    print("Usted aprobo la materia.")
else:
    print("Usted promociono la materia.")
