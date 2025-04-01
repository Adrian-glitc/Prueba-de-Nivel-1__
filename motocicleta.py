from Bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, velocidad, cilindrada, tipo, marca, modelo):
        super().__init__(marca, modelo,color, tipo, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} Km/hr, Cilindrada: {self.cilindrada} cc, Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}"

    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")