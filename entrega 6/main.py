#EJERCICIO 1
from math import sqrt

x1 = float(input("Ingrese los valores del punto x1: "))
x2 = float(input("Ingrese los valores del punto x2: "))

y1 = float(input("Ingrese los valores del punto y1: "))
y2 = float(input("Ingrese los valores del punto y2: "))

punto1 = x2 - x1
punto2 = y2 - y1
distacia = sqrt((punto1)**2 + (punto2)**2)
print("La distacia entre los 2 puntos es: ", distacia)

#EJERCICIO 2
def volumen_y_superficie (alto, largo, profundidad):
        volumen = alto * largo * profundidad
        volumen_en_litros = volumen / 1000
        superficie = alto + largo + profundidad
        resultado = f"El volumen en litros es de {volumen_en_litros} y la superfice de {superficie}"
        return resultado

alto = float(input("Ingrese el alto de la caja en centimetros: "))
largo = float(input("Ingrese el largo de la caja en centimetros: "))
profundidad = float(input("Ingrese la profundidad de la caja en centimetros: "))

print(volumen_y_superficie(alto, largo, profundidad))

#EJERCICIO 3
import string

abecedario = list(string.ascii_lowercase)

def encriptar(abecedario, clave, mensaje):
    mensaje_encriptado = ""
    for letra in mensaje:
        if letra in abecedario:
            e = abecedario.index(letra)
            i = e + clave
            if i > 25:
                i -= 26
            mensaje_encriptado += abecedario[i]
    return mensaje_encriptado

def decodificar(abecedario, clave, mensaje_encriptado):
    mensaje_decodificado = ""
    for letra in mensaje_encriptado:
        if letra in abecedario:
            i = abecedario.index(letra)
            e = i - clave
            if e < 0:
                e += 26
            mensaje_decodificado += abecedario[e]
        else:
            mensaje_decodificado += letra
    return mensaje_decodificado


mensaje = input("Ingrese el mensaje que desea encriptar: ")
clave = int(input("Ingrese la clave: "))

mensaje_encriptado = encriptar(abecedario, clave, mensaje)
mensaje_desencriptado = decodificar(abecedario, clave, mensaje_encriptado)

print(mensaje_encriptado)
print(mensaje_desencriptado)

#EJERCICIO 4
def nombres_y_apellido(primer_nombre, segundo_nombre, apellido):
    if len(segundo_nombre) >= 1:
        segundo_nombre = list(segundo_nombre)
        segundo_nombre[1] = "."
        inicial = segundo_nombre[0] + segundo_nombre[1]
        segundo_nombre = str(inicial)
    x = []
    x.extend([primer_nombre, segundo_nombre, apellido])
    nombre_completo = " ".join(x)
    return nombre_completo

primer_nombre = input("Ingrese su primer nombre: ")
segundo_nombre = input("Ingrese su segundo nombre: ")
apellido = input("Ingrese su apellido: ")
print(nombres_y_apellido(primer_nombre.capitalize(),
      segundo_nombre.capitalize(), apellido.capitalize()))

#EJERCICIO 5
def cantidad_de_rollos(alto, ancho, largo_rollo, ancho_rollo):
    superficie_de_paredes = alto * ancho
    capacidad_del_rollo = largo_rollo * ancho_rollo
    rollos = superficie_de_paredes / capacidad_del_rollo
    return rollos

alto = float(input("Ingrese el alto de la habitacion en metros: "))
ancho = float(input("Ingrese la ancho de la habitacion en metros (recuerde que es la suma del largo de todas sus paredes): "))
largo_rollo = float(input("Ingrese el largo del rollo: "))
ancho_rollo = float(input("Ingrese el ancho del rollo: "))

print(f"Los rollos necesarios son : {cantidad_de_rollos(alto, ancho, largo_rollo, ancho_rollo)}")

