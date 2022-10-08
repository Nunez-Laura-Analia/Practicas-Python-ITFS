# EJERCICIO 1
vector = []
for n in range(5):
    nuevo = float(input("Ingrese el siguiente número:"))
    vector.append(nuevo)
menor = vector[0]
for elemento in vector:
    if elemento < menor:
        menor = elemento
print("El número menor es:", menor)

#EJERCICIO 2
vector = [1, 5, 9, 10, 8]
mayor = vector[0]
for elemento in vector:
    if elemento > mayor:
        mayor = elemento
print("El número mayor es:", mayor)

# EJERCICIO 3
vector = [5, 9, 15, 2, -8, 3]
mayor = vector[0]
for elemento in vector:
    if elemento > mayor:
        mayor = elemento
        
menor = vector[0]
for elemento in vector:
    if elemento < menor:
        menor = elemento
print(f"El número mayor es: {mayor} y el menor es: {menor}")

#EJERCICIO 4
vector = [-5, -9, -15, -2, -8, -3]
mayor = vector[0]
for elemento in vector:
    if elemento > mayor:
        mayor = elemento
        
menor = vector[0]
for elemento in vector:
    if elemento < menor:
        menor = elemento
print(f"El número mayor es: {mayor} y el menor es: {menor}")

#EJERCICIO 5
vector = [1, 5, 9, 10, 8]
mayor1 = vector[0]
for elemento in vector:
    if elemento > mayor1:
        mayor1 = elemento
        
mayor2 = vector[0]
for elemento in vector:
    if elemento >= mayor1:
        mayor1 = elemento
print(f"El dos números mayores son: {mayor1} y {mayor2}")

#EJERCICIO 6
vector = [5,-2, 8, 10, -4, 13, 21]
nuevoVector = []
for elemento in vector:
    nuevoElemento = elemento + 2
    nuevoVector.append(nuevoElemento)
print(vector, nuevoVector)

#EJERCICIO 7
vector = []
for n in range(10):
    nuevo = float(input("Ingrese el siguiente número:"))
    vector.append(nuevo)

mayor = vector[0]
for elemento in vector:
    if elemento > mayor:
        mayor = elemento
        
menor = vector[0]
for elemento in vector:
    if elemento < menor:
        menor = elemento
        
print(f"El número mayor es: {mayor} y el menor es: {menor}")

#EJERCICIO 8
vector = []
for n in range(3):
    nuevo = float(input("Ingrese el siguiente número:"))
    vector.append(nuevo)   
sumaTotal = 0
for elemento in vector:
    sumaTotal = elemento + sumaTotal
promedio = sumaTotal / len(vector) 
print(f"El promedio es: {promedio}")

#EJERCICIO 9
vector = []
nuevo = None 
while nuevo != 0:
    nuevo = float(input("Ingrese el siguiente número:"))
    if nuevo == 0:
        break
    else:
        vector.append(nuevo)
    
mayor = vector[0]
for elemento in vector:
    if elemento > mayor:
        mayor = elemento
        
menor = vector[0]
for elemento in vector:
    if elemento < menor:
        menor = elemento
        
sumaTotal = 0
for elemento in vector:
    sumaTotal = elemento + sumaTotal
promedio = sumaTotal / len(vector) 
        
print(f"El número mayor es: {mayor}, el menor es: {menor} y el promedio es {promedio}")

#EJERCICIO 10
vector = []
nuevo = None 
while nuevo > 0:
    nuevo = float(input("Ingrese el siguiente número:"))
    if nuevo < 0:
        break
    else:
        vector.append(nuevo)

for n in range(len(vector)):
    diferencia = vector[n]
    for elemento in vector:
        elemento = elemento - diferencia
    
print(f"La diferencia de los elementos es: {elemento}") 