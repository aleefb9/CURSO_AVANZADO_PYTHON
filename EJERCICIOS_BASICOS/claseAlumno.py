class Alumno():
    def __init__(self, nombre, calificacion):
        self.nombre = nombre 
        self.calificacion = calificacion

    def __str__(self):
        return "El alumno {}, ha sacado un {}".format(self.nombre, self.calificacion)
    
    def aprobado(self):
        if self.calificacion > 4:
            return True
        else:
            return False

alumno1 = Alumno('Pepe', 5)
print(alumno1)

aprobado = alumno1.aprobado()
if aprobado:
    print("esta aprobado")
else: 
    print("esta suspenso")