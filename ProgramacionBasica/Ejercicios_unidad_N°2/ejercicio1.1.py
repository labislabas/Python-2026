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
temperaturas = [12.5, 14.2, 11.8]

t1 = temperaturas[0]
t2 = temperaturas[1]
t3 = temperaturas[2]

o1 = (t1 + t2 + t3) / 3    #OPERACION 1
o2 = t2 - t3               #OPERACION 2

print(f"El promedio de las temperaturas en la semana es de: {o1:.4} | La diferencia entre el dia con la temperatura mas alta y la mas baja respectivamente es de: {o2:.2}")
