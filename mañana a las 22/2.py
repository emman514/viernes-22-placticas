print("")#espacio en blanco
print("castruita soto emmanuel 3w 1176")#implime nombre 
print("")#espacio en blanco 
class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# Solicitar datos de entrada
nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))

# Crear objeto Persona
p = Persona(nombre, edad)

# Simular dos cumpleaños
p.cumpleaños()
p.cumpleaños()

# Mostrar el resultado
print(f"{p.nombre} cumple {p.edad} años")
