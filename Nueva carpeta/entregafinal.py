from datetime import date, datetime, timedelta
import math

today = date.today()
now = datetime.now()


class Supervisor:
    def _init_(self, nombre: str, apellido: str, auto):
        self.nombre = nombre
        self.apellido = apellido
        self.auto = auto


class Vehiculo:
    def _init_(self, marca: str, modelo: str, patente):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente

    def km_Actual(self):
        self.kmActual = int(
            input("                Ingresa el km del mes pasado: "))
        # self.kmActual=int(dato1.get())

    def kilometro(self):
        self.ultKm = int(input("                Ingresa el km actual: "))
        # self.ultKm=int(dato2.get())
        self.kmAnterior = self.kmActual
        self.kmActual = self.ultKm
        print(self.kmAnterior, self.kmActual)

    def aceiteFiltro(self):
        self.valorAceite = 20000
        print("                ___")
        self.ultAceite = int(
            input("                Ingrese el ultimo cambio de aciete: "))
        # self.ultAceite=int(aceite.get())
        self.proxAceite = self.ultAceite+10000
        self.tiempoAceite = self.proxAceite-self.kmActual

        if self.kmActual < self.proxAceite:
            self.tiempoAceite = self.proxAceite-self.kmActual

            print("\n                Para su proximo cambio de haciente le falta recorrer: ", self.tiempoAceite, "KM",
                  "\n                El proximo cambio de aceite seran: $", self.valorAceite)
            print("____")
            return self.tiempoAceite
            # resultado.set(self.tiempoAceite)
        else:
            self.tiempo_Aceite = self.proxAceite-self.kmActual
            print("                Se paso de su cambio de aceite :",
                  self.tiempo_Aceite, "km")
            return self.tiempo_Aceite
            # resultado.set(self.tiempoAceite)

    def recorrido(self):
        self.diferencia = self.kmActual-self.kmAnterior
        self.diario = self.diferencia/25
        print("___")
        print("                Por mes realiza un estimado de",
              self.diferencia, "km al mes")
        print("                Km recorrido diario :", self.diario, "Km")
        print("___")

    def correa(self):
        self.valorCorrea = 80000
        print("___")
        self.ultCorrea = int(
            input("                Ingrese el ultimo cambio de correa: "))
        self.proxCorrea = self.ultCorrea+60000
        self.tiempoCorrea = self.proxCorrea-self.kmActual
        if self.kmActual < self.proxCorrea:
            print("\n                El proximo cambio de correas es a los", self.proxCorrea, "Km, le faltan", self.tiempoCorrea, "Km",
                  "\n                Tiene un valor de $", self.valorCorrea)
        else:
            print("               Se paso el cambio de correas hace:",
                  self.tiempoCorrea, "Km")
        print("___")

    def cableBujia(self):
        self.valorCable = 40000
        print("___")
        self.ultBujia = int(
            input("                Ingrese el ultimo cambio de bujia : "))
        self.proxBujia = self.ultBujia+30000
        self.tiempoBujia = self.proxBujia-self.kmActual
        # print(self.tiempoBujia)
        if self.kmActual > self.proxBujia:
            print("Se paso del cambio de bujias", self.tiempoBujia, "km")
        if self.kmActual < self.proxBujia:
            print("\n                Su proximo cambio de bujias es a los ", self.proxBujia, "km, le faltan", self.tiempoBujia,
                  "\n                Tiene un valor de $", self.valorCable)
        print("___")

    def neumaticos(self):
        print("___")
        self.valorNeumatico = 200000
        self.ultNeumatico = int(
            input("                Ingrese su ultimo cambio de neumaticos :"))
        self.proxNeumatico = self.ultNeumatico+50000
        self.tiempoNeumatico = self.proxNeumatico-self.kmActual
        if self.kmActual < self.proxNeumatico:
            print("\n                Su proximo cambio de neumaticos es a los ", self.proxNeumatico, "km, le faltan", self.tiempoNeumatico,
                  "\n                Tiene un valor de $", self.valorNeumatico)
        else:
            print("                se paso ", self.tiempoNeumatico, "km")
        print("___")

    def vtv(self):
        print("                ¿Realizo la vtv? :")
        self.si = int(input("                1.SI  2.NO"))
        if self.si == 1:
            self.si = True
        elif self.si != 1:
            self.si = False
            print(
                "               Chequear en la pagina del estado, cuando le corresponde sacar turno.")

        while self.si:
            try:
                self.tiempo = input(
                    "\n                Ingrese su ultima VTV realizada, Ej --> 18/01/1952:")
                self.ultVtv = datetime.strptime(self.tiempo, "%d/%m/%Y")
                self.proxVtv = self.ultVtv+timedelta(days=365)
                print(
                    "                La proxima vtv, se realizara en la fecha: ", self.proxVtv)
                break
            except:
                print("\n                No ha ingresado una fecha correcta...")
                print("\n                ", self.ultVtv)


class Gastos:
    def _init_(self, vehiculo):
        self.vehiculo = vehiculo

    def gastosAuto(self):
        self.gastos = []

    def historialAceite(self):
        self.aceiteHistorico = math.floor(self.vehiculo.kmActual / 10000)
        self.precioAceite = self.aceiteHistorico * 20000
        # ((ACA TENGO QUE HACER EL TOTAL DE CAMBIOS X 10k DIVIDIDO LOS KM QUE RECORRE X DIA Y AL RESULTADO SACARLE EL PORCENTAJE ))
        print("                Hasta el momento solo con el aceite gasto: $",
              self.precioAceite,)

    def historialCorrea(self):
        self.correaHistorico = math.floor(self.vehiculo.kmActual / 60000)
        self.precioCorrea = self.correaHistorico*80000
        print("                Hasta el momento solo con la correa gasto: $",
              self.precioCorrea,)

    def historialBujia(self):
        self.bujiaHistorico = math.floor(self.vehiculo.kmActual / 30000)
        self.precioBujia = self.bujiaHistorico*40000
        print("                Hasta el momento solo con la bujia gasto: $",
              self.precioBujia,)

    def historialNeumatico(self):
        self.neumaticoHistorico = math.floor(self.vehiculo.kmActual / 50000)
        self.precioNeumatico = self.neumaticoHistorico*200000
        print("                Hasta el momento solo con los neumaticos gasto: $",
              self.precioNeumatico,)


Auto1 = Vehiculo("Volkswagen", "Gold Trend", "AB234MK")
Auto2 = Vehiculo("Renault", "Megane", "OXQ291")
Auto3 = Vehiculo("Ford", "Ka", "AA397GS")
Auto4 = Vehiculo("Chevrolete", "Onix", "AE414MP")
Gasto1 = Gastos(Auto1)
Gasto2 = Gastos(Auto2)
Gasto3 = Gastos(Auto3)
Gasto4 = Gastos(Auto4)

Loyola1 = Supervisor("Eduardo", "loyola", Auto1)
Maciel1 = Supervisor("Claudio", "maciel", Auto2)
Gajardo1 = Supervisor("Lucciano", "gajardo", Auto3)
Velazquez1 = Supervisor("Jorge", "velazquez", Auto4)
lista2 = [Auto1, Auto2, Auto3, Auto4]
lista = [Loyola1, Maciel1, Gajardo1, Velazquez1]


comienzo: 0

## COMIENZO DE PROGRAMA ##
print(" \n                 ♦ Ingrese su APELLIDO :",)


def pregunta(apellido1):
    si = True

    while si:
        if apellido1 == Loyola1.apellido:
            print("                Bienvenido ", Loyola1.nombre)
            Auto1.km_Actual()
            Auto1.kilometro()
            si = False
        elif apellido1 == Velazquez1.apellido:
            print("                Bienvenido ", Velazquez1.nombre)
            Auto4.km_Actual()
            Auto4.kilometro()
            si = False
        elif apellido1 == Gajardo1.apellido:
            print("                Bienvenido ", Gajardo1.nombre)
            Auto3.km_Actual()
            Auto3.kilometro()
            si = False
        elif apellido1 == Maciel1.apellido:
            print("                Bienvenido ", Maciel1.nombre)
            Auto2.km_Actual()
            Auto2.kilometro()
            si = False
        else:
            print("              Ingreso mal el apellido")
        break

    print("                     ____")


apellido1 = str(input("          :        ")).lower()

verga = pregunta(apellido1)
# novo=correrGasto(apellido1)
#### COMUNICACION CON LA CONSOLA #####


def pregunta(a):
    arranque = True
    while arranque:
        print("\n                INDIQUE QUE QUIERE SABER :",
              "\n                1. Kilometro anterior y actual del Vehiculo",
              "\n                2. Proximo cambio de ACEITE",
              "\n                3. Proximo cambio de CORREA ",
              "\n                4. Proximo cambio de CABLE Y BUJIA",
              "\n                5. Proximo cambio de NEUMATICO",
              "\n                6. Proxima VTV",
              "\n                7. Kilometros recorridos diarios/mensual",
              "\n                8. Cerrar sesion")
        opcion = int(input(":"))
        if opcion == 1:
            a.km_Actual()
            a.kilometro()
        elif opcion == 2:
            a.aceiteFiltro()
        elif opcion == 3:
            a.correa()
        elif opcion == 4:
            a.cableBujia()
        elif opcion == 5:
            a.neumaticos()
        elif opcion == 6:
            a.vtv()
        elif opcion == 7:
            a.recorrido()
        elif opcion == 8:
            arranque = False


def correrGasto(a):
    arranque = True
    while arranque:
        print("\n                INDIQUE QUE QUIERE SABER :",
              "\n                1. Gasto total de aceite",
              "\n                2. Gasto total de correa",
              "\n                3. Gasto total de bujias",
              "\n                4. Gasto total de neumaticos",
              "\n                5. Cerrar sesion")
        opcion = int(input(":"))
        if opcion == 1:
            a.historialAceite()
        elif opcion == 2:
            a.historialCorrea()
        elif opcion == 3:
            a.historialBujia()
        elif opcion == 4:
            a.historialNeumatico()
        elif opcion == 5:
            print("                      A R S E C")
            arranque = False
#################################################


# INICIACION PARA LA CONSOLA
for n in lista:
    n = apellido1
    if apellido1 == Loyola1.apellido:
        vergax = pregunta(Auto1)
        novo = correrGasto(Gasto1)
    elif apellido1 == Maciel1.apellido:
        vergax = pregunta(Gasto2)
        novo = correrGasto(Auto2)
    elif apellido1 == Velazquez1.apellido:
        vergax = pregunta(Auto4)
        novo = correrGasto(Gasto4)
    elif apellido1 == Gajardo1.apellido:
        vergax = pregunta(Auto3)
        novo = correrGasto(Gasto3)

    break
