class Automovil:
    def __init__(self, color, marca, aceleracion, velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self.ruedas = 4

    def acelera(self):
        self.velocidad += self.aceleracion

    def frena(self):
        self.velocidad -= self.aceleracion
