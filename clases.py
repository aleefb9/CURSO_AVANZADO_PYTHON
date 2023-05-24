class Vehiculo:
    def __init__(self,color,velocidadMaxima,marca):
        self.color = color
        self.velocidadMaxima = velocidadMaxima
        self.velocidad = 0
        self.marca = marca

    def arrancar(self):
        print('Arrancado')

    def acelerar(self):
        if self.velocidad == 0:
            self.velocidad = self.velocidad + 10
        else:
            self.velocidad = self.velocidad + 10
        print('Velocidad = ', self.velocidad)

    def frenar(self):
        if self.velocidad > 10:
            self.velocidad = self.velocidad - 10
        else:
            self.velocidad = 0
        print('Velocidad = ', self.velocidad)

    def nuestroEstado(self):
        print(f'Soy de la marca {self.marca}, de color {self.color} y velocidad máxima de {self.velocidadMaxima}')

peugeot = Vehiculo('rojo', 120, 'Peugeot')
peugeot.arrancar()
peugeot.acelerar()
peugeot.nuestroEstado()
peugeot.acelerar()

renault = Vehiculo('verde', 150, 'Renault')
renault.arrancar()
renault.acelerar()
renault.nuestroEstado()
renault.acelerar()