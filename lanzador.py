from Coche import Coche
from Bicicleta import Bicicleta
from Camioneta import Camioneta
from motocicleta import Motocicleta
from Vehiculo import Vehiculo

def lanzador_main():
    vehiculos = [
        Coche("Rojo", 4, "Gasolina", 150),
        Coche("Azul", 4, "Diesel", 180),
        Coche("Negro", 4, "Eléctrico", 200),
        Coche("Blanco", 4, "Híbrido", 170),
        Coche("Gris", 4, "Gasolina", 160),
        Bicicleta("lujo", "Montaña", "Verde", "Urbana", 2),
        Bicicleta("estándar", "Carretera", "Amarillo", "Deportiva", 2),
        Bicicleta("lujo", "Eléctrica", "Negro", "Urbana", 2),
        Bicicleta("estándar", "Plegable", "Blanco", "Recreativa", 2),
        Bicicleta("lujo", "BMX", "Rojo", "Deportiva", 2),
        Camioneta("Negro", 4, 200, 1000, "Ford", 2015, 120),
        Camioneta("Blanco", 4, 250, 1200, "Chevrolet", 2018, 130),
        Camioneta("Gris", 4, 220, 1100, "Toyota", 2020, 140),
        Camioneta("Azul", 4, 240, 1300, "Nissan", 2017, 125),
        Camioneta("Rojo", 4, 210, 1150, "Honda", 2019, 135),
        Motocicleta("Blanca", 2, 180, 1000, "Deportiva", "Yamaha", 2015),
        Motocicleta("Negra", 2, 200, 1200, "Cruiser", "Harley-Davidson", 2018),
        Motocicleta("Roja", 2, 220, 900, "Naked", "Kawasaki", 2020),
        Motocicleta("Azul", 2, 190, 1100, "Touring", "BMW", 2017),
        Motocicleta("Gris", 2, 210, 950, "Sport", "Ducati", 2019),
    ]
    return vehiculos

def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print(f"Clase: {vehiculo.__class__.__name__}")
        for atributo, valor in vehiculo.__dict__.items():
            print(f"{atributo}: {valor}")
        print()

def catalogar_ruedas(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [v for v in vehiculos if getattr(v, 'ruedas', None) == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()
    else:
        for vehiculo in vehiculos:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()




# Ejecución de las funciones
lanzador_main()