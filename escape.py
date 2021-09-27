import math

# Lectura de datos de entrada
g = float(input("Ingrese la constante g:\n"))
r = int(input("Ingrese el radio en Kilometros (Km)\n"))

# radio a metros
r = (r * 1000)

# Calcular velocidad de escape
velocidad_escape = math.sqrt(2 * g * r)

print(f"La velocidad de escape es de {velocidad_escape}")

