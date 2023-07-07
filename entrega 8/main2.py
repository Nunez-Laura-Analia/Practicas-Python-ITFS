class Pared:
    def __init__(self, largo, alto):
        self.largo = largo
        self.alto = alto
        self.superficie = self.calcular_superficie()

    def calcular_superficie(self):
        return self.largo * self.alto
    
class Abertura:
        def __init__(self, largo_abertura, alto_abertura):
            self.largo_abertura = largo_abertura
            self.alto_abertura = alto_abertura
            self.superficie = self.calcular_superficie()

        def calcular_superficie(self):
            return self.largo_abertura * self.alto_abertura

class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paredes = []
        self.aberturas = []

    def agregar_pared(self, largo, alto):
        pared = Pared(largo, alto)
        self.paredes.append(pared)
        
    def agregar_abertura(self, largo_abertura, alto_abertura):
        abertura = Abertura(largo_abertura, alto_abertura)
        self.aberturas.append(abertura)

    def superficie_aberturas(self):
        superficie_total_de_aberturas = 0
        for abertura in self.aberturas:
            superficie_total_de_aberturas += abertura.superficie
        return superficie_total_de_aberturas
    
    def superficie_total_de_pared(self):
        superficie_total_de_pared = 0
        for pared in self.paredes:
            superficie_total_de_pared += pared.superficie
        return superficie_total_de_pared
    
    def superficie_total_a_pintar(self):
        superficie_pared = self.superficie_total_de_pared()
        superficie_abertura = self.superficie_aberturas()
        superfie_total_a_pintar = superficie_pared - superficie_abertura
        return superfie_total_a_pintar
        
    def calcular_litros_pintura(self, rendimiento_litros):
        superficie_total = self.superficie_total_a_pintar()
        litros_pintura = superficie_total / rendimiento_litros
        return litros_pintura

habitacion1 = Habitacion("Sala")

habitacion1.agregar_pared(5, 4) 
habitacion1.agregar_pared(5, 4)  
habitacion1.agregar_pared(5, 4)
habitacion1.agregar_pared(5, 4)  

habitacion1.agregar_abertura(2, 5)

rendimiento_litros = 10
superficie_total = habitacion1.superficie_total_a_pintar()
litros_pintura = habitacion1.calcular_litros_pintura(rendimiento_litros)

print("La superficie total a pintar en la habitación es de:", superficie_total, "metros cuadrados")
print("Los litros de pintura necesarios son:", litros_pintura)