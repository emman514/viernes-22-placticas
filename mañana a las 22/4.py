print("")#espacio en blanco
print("castruita soto emmanuel 3w 1176")#implime nombre 
print("")#espacio en blanco 
class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)
class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)  # Llama al constructor de la clase base (Persona)
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)
# Ejemplo de uso:
persona = Persona("Juan", "Pérez")
persona.nombre_completo()  # Debería imprimir: Juan Pérez

estudiante = Estudiante("María", "González", "Ingeniería de Sistemas")
estudiante.nombre_completo()  # Debería imprimir: María González
estudiante.mostrar_carrera()  # Debería imprimir: Ingeniería de Sistemas
