"""El Departamento de Informática de la Universidad de Los Lagos está monitoreando el consumo de
memoria RAM (en Gigabytes) de uno de sus servidores principales de bases de datos. Se han
registrado los consumos exactos en 4 instantes del día (Mañana, Mediodía, Tarde y Noche) dentro
de una lista de Python.
Escribe un programa en Python que realice las siguientes tareas utilizando exclusivamente lo
aprendido hasta el momento en la Unidad II:
1.Ingresar por terminal los 4 consumos del día y guardarlo en una lista con valores de tipo
decimal (float).
2.Acceder a cada valor individualmente utilizando la indexación de listas para guardarlos en
variables independientes.
3.Calcule y muestre el consumo promedio de RAM del servidor durante el día.
4.Calcule y muestre el 'Rango de Operación' (la diferencia entre el consumo máximo y el mínimo
detectado) haciendo uso de las funciones integradas de Python vistas en clases."""

madrugada = float(input("Ingrese el consumo de RAM por la madrugada: "))
print(madrugada)

medio= float(input("Ingrese el consumo de RAM por la madrugada: "))
print(medio)

tarde = float(input("Ingrese el consumo de RAM por la madrugada: "))
print(tarde)

noche = float(input("Ingrese el consumo de RAM por la madrugada: "))
print(noche)

ram = list([madrugada,medio,tarde,noche])

r1 = ram[0]
r2 = ram[1]
r3 = ram[2]
r4 = ram[3]

o1 = (r1 + r2 + r3 +r4) / 4    #OPERACION 1
o2 = max(ram) - min(ram)       #OPERACION 2

print(f"El consumo promedio de RAM del servidor durante el dia es de: {o1} | La diferencia entre el consumo maximo y minimo detectado es de: {o2}")






