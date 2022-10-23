# EJERCICIO 1
def fecha_valida(dia, mes, anio):
    validez = True
    bisiesto = False
    meses_con_31 = [1, 3, 5, 7, 8, 10, 12]
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        bisiesto = True
    if (dia > 31 or dia < 1) or (mes > 12 or mes < 1) or (anio > 2022 or anio < 1582) or (bisiesto == False and dia > 28):
        validez = False
        return validez
    elif(dia == 31 and mes in meses_con_31):
        return validez 
    else:
        return validez

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
if (fecha_valida(dia, mes, anio)):
    print("La fecha ingresada es valida.")
else:
    print("La fecha ingresada es invalida.")

# EJERCICIO 2
segundos = int(input("Ingrese el tiempo en segundos:"))
horas = segundos//3600
sobrante1 = segundos % 3600
minutos = sobrante1//60
sobrante2 = sobrante1 % 60
print(f"{horas} : {minutos} : {sobrante2}")


# EJERCICIO 3
for i in range(0, 7):
    for e in range(0, i + 1):
        print(f"| {i} | {e} |")

# EJERCICIO 4


def empaquetado(pesoPorPaquete):
    pesoAcumulado = 0
    while pesoAcumulado < pesoPorPaquete:
        pesoAcumulado += int(input("Ingrese el peso acumulado hasta ahora de galletitas: "))
        if pesoAcumulado > pesoPorPaquete:
            cantidad_a_sacar = pesoAcumulado - pesoPorPaquete
    return f"Debe cambiarse el paquete. Se superaron los {pesoPorPaquete}. Debe sacar {cantidad_a_sacar} y ponerlos en un nuevo paquete."


pesoPorPaquete = int(input("Ingrese el peso que debe tener el paquete: "))
print(empaquetado(pesoPorPaquete))

# EJERCICIO 5


def empaquetado(capacidadDelSilo):
    cantidadDeHarinaInicial = int(
        input("Ingrese la cantidad de harina inicial dentro del silo: "))
    if cantidadDeHarinaInicial > capacidadDelSilo:
        return "Los datos ingresados son incorrectos, vuelva a intentarlo."
    else:
        cantidadDeHarinaRequerida = 0
        while cantidadDeHarinaRequerida < cantidadDeHarinaInicial:
            cantidadDeHarinaRequerida += int(
                input("Ingrese la cantidad de harina requerida para la preparacion: "))
            cantidadRestante = cantidadDeHarinaInicial - cantidadDeHarinaRequerida
            nuevaCapacidad = capacidadDelSilo - cantidadRestante
            if (cantidadDeHarinaRequerida <= cantidadDeHarinaInicial):
                print(
                    f"La cantidad es suficiente. La nueva capacidad es de {nuevaCapacidad} y la harina restante es de {cantidadRestante}")
            else:
                break
        return "Ya no hay cantidad de harina sufucuente para una nueva preparacion."


capacidadDelSilo = int(input("Ingrese la capacidad del silo: "))
print(empaquetado(capacidadDelSilo))
