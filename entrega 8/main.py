#EJERCICIO 1
import numpy as np

v = np.random.rand(10)
normalized_v = v/np.linalg.norm(v)
print(normalized_v)

#EJERCICIO 2
lista = [1,2,5,"hola", "programacion", 1, 2, "hola"]
conjunto = set(lista)
lista = list (conjunto)
print(lista)

#EJERCICIO 3
tablero =[  "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
def ver_tablero():
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " +  tablero[2]  +"       1 | 2 | 3")
    print(tablero[3] + " | " + tablero[4] + " | " +  tablero[5]  +"       4 | 5 | 6")
    print(tablero[6] + " | " + tablero[7] + " | " +  tablero[8]  +"       7 | 8 | 9")
    print("\n")

def jugada(valor):
    anoto = False
    while anoto==False:
        posicion = int(input("Elegí una posicion del 1 al 9: "))
        posicion -= 1
        if tablero[posicion] == "-":
            anoto = True
        else:
            print("Lo siento, esta posicion ya esta ocupada. ¡Elegí otra!")
    tablero[posicion] = valor
    ver_tablero()
    
def jugar():
    print("¡Que empiece el juego!")
    ver_tablero()
    for i in range(4):
        print("Es el turno del jugador 1 - X")
        valor="X"
        jugada(valor)
        print("Es el turno del jugador 2 - O")
        valor="O"
        jugada(valor)
    print("Turno del jugador 2 - X")
    valor="X"
    jugada(valor)        
jugar()        

#EJERCICIO 4
tablero =[  "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
ganador = None
def jugar():
    global ganador
    print("Que empiece el juego!")
    ver_tablero()
    for i in range(5):
        print("Es el turno del jugador 1 - X")
        valor="X"
        jugada(valor)
        huboGanador()
        if ganador != "X" and i < 4 :
            for j in range(3):
                print("Es el turno del jugador 2 - O")
                valor="O"
                jugada(valor)
                huboGanador()
                if ganador == "O":
                    print("¡Felicadades! El ganador del TA-TE-TI es el jugador número 2")
                break
        elif ganador=="X":
            print("¡Felicadades! El ganador del TA-TE-TI es el jugador número 1")
            break
        else:
            print("¡Ambos jugadores empataron!")
def huboGanador():
    global ganador
    controlLinea()
    controlVertical()
    controlDiagonal()
def controlLinea():
    global ganador
    if tablero[0]== tablero[1]==tablero[2] !="-":
        ganador = tablero[0]
    elif tablero[3] ==  tablero[4] == tablero[5] != "-":
        ganador = tablero[3]
    elif tablero[6] ==  tablero[7] == tablero[8] != "-":
        ganador = tablero[6]
def controlVertical():
    global ganador
    if tablero[0] ==  tablero[3] == tablero[6] != "-":
        ganador = tablero[0]
    elif tablero[1] ==  tablero[4] == tablero[7] != "-":
        ganador = tablero[1]
    elif tablero[2] ==  tablero[5] == tablero[8] != "-":
        ganador = tablero[2]
def controlDiagonal():
    global ganador
    if tablero[0] ==  tablero[4] == tablero[8] != "-":
        ganador = tablero[0]
    elif tablero[2] ==  tablero[4] == tablero[6] != "-":
        ganador = tablero[2]
def jugada(valor):
    anoto = False
    while anoto==False:
        posicion = int(input("Elegí una posicion del 1 al 9: "))
        posicion -= 1
        if tablero[posicion] == "-":
            anoto = True
        else:
            print("Lo siento, esta posicion ya esta ocupada. ¡Elegí otra!")
    tablero[posicion] = valor
    ver_tablero()
def ver_tablero():
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " +  tablero[2]  +"       1 | 2 | 3")
    print(tablero[3] + " | " + tablero[4] + " | " +  tablero[5]  +"       4 | 5 | 6")
    print(tablero[6] + " | " + tablero[7] + " | " +  tablero[8]  +"       7 | 8 | 9")
    print("\n")
jugar()

#EJERCICIO 5
n = int(input("Ingrese el número de vértices del polígono: "))

x = []
y = []

for i in range(n):
    coordenada_x = int(input(f"Ingrese el valor de la coordenada x{i}: "))
    coordenada_y = int(input(f"Ingrese el valor de la coordenada y{i}: "))
    x.append(coordenada_x)
    y.append(coordenada_y)

x.append(x[0])
y.append(y[0])

vertices = list(zip(x, y))
print(vertices)

for i in range(n):
    suma = (x[i] * (y[i+1] - y[i-1]))

Área_Polígono = (1/2)*abs(suma)

print("Área del polígono=:", Área_Polígono, "U^2")
