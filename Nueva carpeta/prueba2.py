# class Pedido:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio


# class Mesa:
#     def __init__(self, numero):
#         self.numero = numero
#         self.pedidos = []

#     def agregar(self, nombre, precio):
#         pedido = Pedido(nombre, precio)
#         self.pedidos.append(pedido)

#     def calcular_total(self):
#         total = 0
#         for pedido in self.pedidos:
#             total += pedido.precio
#         return total


# # Se crea cada mesa
# mesa1 = Mesa(1)
# mesa2 = Mesa(2)
# mesa3 = Mesa(3)

# # Se cargar los pedidos
# mesa1.agregar("Ensalada", 2500)
# mesa1.agregar("Filete", 2300)

# mesa2.agregar("Hamburguesa", 3200)
# mesa2.agregar("Pasta", 2500)

# mesa3.agregar("Ensalada", 1800)
# mesa3.agregar("Jugo", 1200)

# # Se calcula el total por mesa
# total_mesa1 = mesa1.calcular_total()
# total_mesa2 = mesa2.calcular_total()
# total_mesa3 = mesa3.calcular_total()

# # Se imprime el total de cada mesa
# print("Total a pagar en la mesa 1:", total_mesa1)
# print("Total a pagar en la mesa 2:", total_mesa2)
# print("Total a pagar en la mesa 3:", total_mesa3)


def elegirAuto(listaDeAutos):
    auto_elegido = input(
        "Elija el numero de auto. Por ejemplo, si quiere saber los datos del auto 1, presione el numero 1")
    if auto_elegido == 1:
        return listaDeAutos[0]
    elif auto_elegido == 2:
        return listaDeAutos[1]
    else:
        return print("Ha ocurrido un error, vuelva a intentarlo.")


auto1 = ["Volkswagen", "Gold Trend", "AB234MK",
                     50000, 55000, 60, 60, 60, 60, 60, 11/5/2019]
auto2 = ["Renault", "Megane", "OXQ291",
                 50000, 55000, 60, 60, 60, 60, 60, 15/12/2020]
lista= [auto1, auto2]

print(elegirAuto(lista))

    auto_elegido = input(
        "Elija el numero de auto. Por ejemplo, si quiere saber los datos del auto 1, presione el numero 1")
    if auto_elegido == 1:
        auto = listaDeAutos[0]
    elif auto_elegido == 2:
        auto = listaDeAutos[1]
    elif auto_elegido == 3:
        auto = listaDeAutos[2]
    elif auto_elegido == 4:
        auto = listaDeAutos[3]
    else:
        print("Ha ocurrido un error, vuelva a intentarlo.")
