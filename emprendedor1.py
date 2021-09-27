import math

# Lectura de datos de entrada
p = int(input("Ingrese el precio de suscripción\n"))
u = int(input("Ingrese el numero de usuarios\n"))
gt = float(input("Ingrese el gasto total\n"))


utilidades = math.sqrt(p * u) - gt


print(f"Las utilidades son {utilidades}")
