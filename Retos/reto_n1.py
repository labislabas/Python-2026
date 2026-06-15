pregunta_1 = float(input("Ingrese su nota del 'laboratorio 1' de forma individual: "))
print(pregunta_1)

pregunta_2 = float(input("Ingrese su nota del 'laboratorio 2' de forma individual: "))
print(pregunta_2)

pregunta_3 = float(input("Ingrese su nota del 'laboratorio 3' de forma individual: "))
print(pregunta_3)

lista_1 = [pregunta_1, pregunta_2, pregunta_3]

promedio_ponderado = (lista_1[0] * 40/100) + (lista_1[1] * 40/100) + (lista_1[2] * 20/100)

print(f"Nota laboratorio 1: {lista_1[0]} | Nota laboratorio 2: {lista_1[1]} | Nota laboratorio 3: {lista_1[2]} | Promedio de sus notas: {promedio_ponderado:.2}")