"""En fisica de particulas, la precision de los decimales es critica. Un sensor de presion
hidraulica en un laboratorio de la universidad entrega una medida de 1024.7689 Pas-
cales como tipo float. Escribe un programa que realice lo siguiente:
a) Defina la variable con el valor del sensor.
b) Convierta dicho valor a un numero entero (int), descartando los decimales, y
almacenelo en una variable nueva.
c) Utilice un metodo propio de Python para redondear el valor original del sensor a
exactamente 2 decimales y guarde el resultado en otra variable.
d ) Imprima un mensaje comparativo que muestre por terminal: el valor original, el
valor truncado como entero y el valor redondeado."""

valor_sensor = 1024.7689
valor_sensor_entero = int(valor_sensor)
redondeado_valor_sensor = round(valor_sensor,2)

print(f"Acontinuacion se mostraram los valores que ha entregado el sensor \n Valor original original(inicial): {valor_sensor} ")
