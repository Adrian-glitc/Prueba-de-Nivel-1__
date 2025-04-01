from Coche import Coche

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, marca, modelo, capacidad_carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.marca = marca
        self.modelo = modelo
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} Km/hr, Cilindrada: {self.cilindrada} cc, Carga: {self.capacidad_carga} Kg"
    
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")