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
print(f"Elconsumo total de RAM es: {consumo_total}")

promedio = consumo_total / 4
print(f"El promedio de la RAM es: {promedio}")

max_ram = max(ram)
print(f"El valor maximo de la RAM ingresado de manera individual es: {max_ram}")





