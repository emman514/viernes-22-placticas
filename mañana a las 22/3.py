print("")  # Espacio en blanco para separar la salida del código que sigue
# Imprime el nombre del autor y el curso o el código de la clase
print("castruita soto emmanuel 3w 1176")  # Imprime el nombre y otros detalles
print("")  # Espacio en blanco para separar la salida del código
# Definición de la clase "Calculadora"
class Calculadora():
    # El método __init__ es el constructor de la clase y se usa para inicializar los atributos.
    def __init__(self, num1, num2):
        self._num1 = num1  # El primer número de la operación
        self._num2 = num2  # El segundo número de la operación
    # Método para realizar la suma
    def suma(self):
        resultado = self._num1 + self._num2  # Suma de los dos números
        print(f"El resultado de la suma es: {self._num1} + {self._num2} = {resultado}")  # Muestra el resultado de la suma
    # Método para realizar la resta
    def resta(self):
        resultado = self._num1 - self._num2  # Resta de los dos números
        print(f"El resultado de la resta es: {self._num1} – {self._num2} = {resultado}")  # Muestra el resultado de la resta
    # Método para realizar la división
    def division(self):
        resultado = self._num1 // self._num2  # División entera de los dos números
        print(f"El resultado de la división es: {self._num1} // {self._num2} = {resultado}")  # Muestra el resultado de la división
    # Método para realizar la multiplicación
    def multiplicacion(self):
        resultado = self._num1 * self._num2  # Multiplicación de los dos números
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")  # Muestra el resultado de la multiplicación
# Instancia de la clase "Calculadora" para realizar la suma
operacion = Calculadora(10, 5)  # Creamos un objeto de la clase Calculadora con los números 10 y 5
operacion.suma()  # Llamamos al método suma para obtener el resultado
# Instancia de la clase "Calculadora" para realizar la resta
operacion = Calculadora(20, 5)  # Creamos un objeto de la clase Calculadora con los números 20 y 5
operacion.resta()  # Llamamos al método resta para obtener el resultado
# Instancia de la clase "Calculadora" para realizar la división
operacion = Calculadora(15, 3)  # Creamos un objeto de la clase Calculadora con los números 15 y 3
operacion.division()  # Llamamos al método division para obtener el resultado
# Instancia de la clase "Calculadora" para realizar la multiplicación
operacion = Calculadora(8, 4)  # Creamos un objeto de la clase Calculadora con los números 8 y 4
operacion.multiplicacion()  # Llamamos al método multiplicacion para obtener el resultado
