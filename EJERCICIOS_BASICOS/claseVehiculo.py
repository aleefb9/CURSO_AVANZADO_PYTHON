class Vehiculo():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def __str__(self):
        return "El vehículo de marca {} es de color {}".format(self.marca, self.color)


class Coche(Vehiculo):
    def __init__(self, marca, color, potencia, motor):
        Vehiculo.__init__(self, marca, color)
        self.potencia = potencia
        self.motor = motor

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} Cv y motor de {}".format(self.potencia, self.motor)

miVehiculo = Vehiculo('Seat', 'Amarillo')
print(miVehiculo)

miCoche = Coche('Seat', 'rojo', '1500', 'gasolina')
print(miCoche)