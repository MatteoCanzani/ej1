class Automovil:
    def __init__(self, color, marca, aceleracion, velocidad):
        self.ruedas = 4
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def mostrar_info(self):
        print("Ruedas:", self.ruedas)
        print("Aceleración:", self.aceleracion)

    def modificar_aceleracion(self, nueva_aceleracion):
        self.aceleracion = nueva_aceleracion
        print("Nueva aceleración:", self.aceleracion)

    def acelerar(self):
        self.velocidad += self.aceleracion

    def frenar(self):
        self.velocidad -= self.aceleracion


auto1 = Automovil(color="Rojo", marca="Toyota", aceleracion=10, velocidad=18)
print("Auto 1:")
auto1.mostrar_info()

auto1.modificar_aceleracion(16)


auto1.acelerar()
print("después de acelerar:", auto1.velocidad)

auto1.frenar()
print("después de frenar:", auto1.velocidad)


auto2 = Automovil(color="Azul", marca="Ford", aceleracion=20, velocidad=50)
print("\nAuto 2 antes de frenar:")
auto2.mostrar_info()
auto2.frenar()
print("Velocidad de Auto 2 después de frenar:", auto2.velocidad)
