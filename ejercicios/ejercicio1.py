"""Un centro de investigación de la Región de Los Lagos registró las
temperaturas de los primeros 3 días de la semana en una lista. Crea un
programa en Python que calcule el promedio de la semana y la
diferencia entre el día más alto y el más bajo usando operaciones de
listas.

Días    Temperaturas (°C)
Lunes       12.5
Martes      14.2
Miércoles   11.8
"""
t = list([12.5, 14.2, 11.8])

n1 = t[0]
n2 = t[1]
n3 = t[2]

s = n1 + n2 + n3 
p = s / 3 

print(f"El promedio de las temperaturas durante la semana es: {p:.3f}")

n4 = n2 - n3

print(f"La diferencia entre el dia con la temperatura mas alta y baja es: {n4:.1f}")