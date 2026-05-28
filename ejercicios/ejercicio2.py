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


manana = float(input("Ingrese el consumo de RAM por la mañana: "))
print(manana)

medio = float(input("Ingrese el consumo de RAM en el mediodía: "))
print(medio)

tarde = float(input("Ingrese el consumo de RAM por la tarde: "))
print(tarde)

noche = float(input("Ingrese el consumo de RAM por la noche: "))
print(noche)

ram = list([manana, medio, tarde, noche])

consumo_ma = ram[0]
consumo_me = ram[1]
consumo_ta = ram[2]
consumo_no = ram[3]


consumo_total = (consumo_ma + consumo_me +consumo_ta + consumo_no)
print(consumo_total)

promedio = consumo_total / 4
print(promedio)

len(ram)


