#La clase Either encapsula un valor que puede ser un resultado exitoso (Right) o un error (Left).
class Either:
    def __init__(self, is_right, value):
        self.is_right = is_right
        self.value = value
    #Este Metodo verifica si el valor es real
    #Either.left(value): Crea una instancia de Either con un valor que representa un error.
    def is_left(self):
        return not self.is_right

    def bind(self, func):
        if self.is_left():
            return self
        else:
            return func(self.value)
    
    @staticmethod
    def left(value):
        return Either(False, value)
    
    @staticmethod
    def right(value):
        return Either(True, value)


# Ejemplo de función que usa Either para gestionar entradas de datos

def safe_divide(x, y):
    if y == 0:
        return Either.left("Error: División por cero")
    elif y is None:
        return Either.left("Error: Valor de entrada es None")
    else:
        return Either.right(x / y)

# Proceso de datos utilizando Either
#Se procesan los datos utilizando la función safe_divide y la mónada Either. Los resultados se almacenan en una lista.

data = [
    (10, 2),
    (4, 0), 
    (8, 4),
    (9, None)  
]

resultados = []

for x, y in data:
    either_result = Either.right(y).bind(lambda val: safe_divide(x, val))
    resultados.append(either_result)

# Evaluación de resultados

for result in resultados:
    if result.is_left():
        print(result.value)
    else:
        print("Resultado:", result.value)
# Se imprimen los resultados, indicando si hubo un error debido a datos incompletos o divisiones no válidas, o el resultado de la operación exitosa.