from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, tipo, ruedas):
        super().__init__(color, ruedas)
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Tipo: {self.tipo}"
    
    @staticmethod
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")