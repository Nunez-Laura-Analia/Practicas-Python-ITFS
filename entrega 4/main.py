# EJERCICIO 1
dia = int(input("Ingrese el dia:"))
mes = int(input("Ingrese el mes:"))
anio = int(input("Ingrese el anio:"))

if (dia > 31 or dia < 1) or (mes > 12 or mes < 1) or (anio > 2022 or anio < 1):
    print("Fecha invalida.")
else:
    print("Fecha valida.")

# EJERCICIO 2


# EJERCICIO 3
for i in range(0, 7):
    for e in range(0, i + 1):
        print(f"| {i} | {e} |")

# EJERCICIO 4
def empaquetado(pesoPorPaquete):
    pesoAcumulado = int(input("Ingrese el peso acumulado de galletitas: "))
    if pesoAcumulado >= pesoPorPaquete:
        print("Debe cambiarse el paquete.")
    else:
        print("Puede seguir usando el mismo paquete.")

pesoPorPaquete = int(input("Ingrese el peso que debe tener el paquete: "))
empaquetado(pesoPorPaquete)

# EJERCICIO 5
def empaquetado(capacidadDelSilo):
    cantidadDeHarina = int(
        input("Ingrese la cantidad de harina dentro del silo: "))
    if cantidadDeHarina > capacidadDelSilo:
        print("Los datos ingresados son incorrectos, vuelva a intentarlo.")
    else:
        cantidadDeHarinaRequerida = int(
            input("Ingrese la cantidad de harina requerida para la preparacion: "))
        if cantidadDeHarinaRequerida < cantidadDeHarina:
            cantidadRestante = cantidadDeHarina - cantidadDeHarinaRequerida
            nuevaCapacidad = capacidadDelSilo - cantidadRestante
            print(
                f"La cantidad es suficiente. La nueva capacidad es de {nuevaCapacidad} y la haria restante es de {cantidadRestante}")
        else:
            print("La cantidad no es la suficiente.")


capacidadDelSilo = int(input("Ingrese la cantidad del silo: "))
empaquetado(capacidadDelSilo)
