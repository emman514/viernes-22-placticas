#espacio en blanco
print("") 
#imprime nombre
print("castruita soto emmanuel 3w 1176") 
#espacio en blanco
print("") 
# Clase base Fabrica
class Fabrica:
    # Constructor con los atributos llantas, color y precio
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
# Clase Moto que hereda de Fabrica
class Moto(Fabrica):
    def cantidad(self):
        # Imprime la cantidad de llantas, color y precio de la moto
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
# Clase Carro que hereda de Fabrica
class Carro(Fabrica):
    def cantidad(self):
        # Imprime la cantidad de llantas, color y precio del carro
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
        print("OBJETO=carro")
# Crear un objeto de la clase Moto
moto = Moto(2, "Gris", "$200")
moto.cantidad()  # Imprimir los detalles de la moto
# Imprimir tipo de objeto
print("OBJETO=moto")
# Crear un objeto de la clase Carro
carro = Carro(4, "Negro", "$600")
carro.cantidad()  # Imprimir los detalles del carro
