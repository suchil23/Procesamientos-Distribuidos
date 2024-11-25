# Práctica DataFlow
# Con la Clase Maybe encapsulamos un valor
class Maybe:
    def __init__(self, value):
        self.value = value
    # El método is_nothing verificara que el valor es None
    def is_nothing(self):
        return self.value is None
    #El método Bind encapsulará la función si el valor es none
    def bind(self, func):
        if self.is_nothing():
            return self
        else:
            return func(self.value)
    
    @staticmethod
    # Se creo una instancia de Maybe con un valor (Value)
    def just(value):
        return Maybe(value)
    # Se creo una instancia de Maybe con None
    @staticmethod
    def nothing():
        return Maybe(None)


# Ejemplo de función que usa Maybe para gestionar entradas de datos
#Se procesan los datos utilizando la función safe_divide y la mónada Maybe. Los resultados se almacenan en una lista
def safe_divide(x, y):
    if y == 0:
        return Maybe.nothing()
    else:
        return Maybe.just(x / y)

# Proceso de datos utilizando Maybe

data = [
    (10, 2),
    (4, 0),  
    (8, 4),
    (9, None) 
]
# Aquí esta la lista donde se van a almacenar los datos
resultados = []

for x, y in data:
    maybe_result = Maybe.just(y).bind(lambda val: safe_divide(x, val))
    resultados.append(maybe_result)

# Evaluación de resultados

for result in resultados:
    if result.is_nothing():
        print("Error: Operación no válida o datos incompletos.")
    else:
        print("Resultado:", result.value)
