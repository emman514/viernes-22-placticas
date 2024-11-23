print("")  # espacio en blanco
print("castruita soto emmanuel 3w 1176")  # imprime nombre
print("")  # espacio en blanco 
# Clase Universidad con el nombre de la universidad
class Universidad:
    def __init__(self, Nombre):
        self.Nombre = Nombre
# Clase Carerra que define la especialidad
class Carerra:
    def __init__(self, especialidad):
        self.especialidad = especialidad
# Clase Estudiante que hereda de Universidad y Carerra
class Estudiante(Universidad, Carerra):
    def __init__(self, Nombre, especialidad, nombre, edad):
        Universidad.__init__(self, Nombre)  # Inicializa Universidad
        Carerra.__init__(self, especialidad)  # Inicializa Carerra
        self.nombre = nombre
        self.edad = edad
    def datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")
# Crear una instancia de Estudiante
persona = Estudiante("Harvard", "Ingeniería Mecatrónica", "Mike", 19)
persona.datos()  # Mostrar los datos del estudiante
