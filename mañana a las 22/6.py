print("")  # espacio en blanco
print("castruita soto emmanuel 3w 1176")  # imprime nombre
print("")  # espacio en blanco 
# Definición de la clase Marino, que será la clase base
class Marino:
    def hablar(self):
        print("Hola soy un animal marino!")
# Clase Pulpo hereda de Marino y redefine el método hablar
class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo!")
# Clase Foca hereda de Marino y redefine el método hablar con un parámetro mensaje
class Foca(Marino):
    def hablar(self, mensaje):
        self.mensaje = mensaje  # Guarda el mensaje
        print(mensaje)
# Crear instancias de cada clase
marino = Marino()  # Instancia de la clase base
marino.hablar()  # Llamar al método hablar de Marino

pulpo = Pulpo()  # Instancia de la clase Pulpo
pulpo.hablar()  # Llamar al método hablar de Pulpo

foca = Foca()  # Instancia de la clase Foca
foca.hablar("Hola soy una foca!")  # Llamar al método hablar de Foca con un mensaje personalizado
