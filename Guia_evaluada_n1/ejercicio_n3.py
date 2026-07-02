# Miembros: Leonardo y Maykol

#Primero ponemos el sueldo base y un diccionario con los datos harcodeeados

SueldoBase_2025 = 529000

Vendedores = {
    "Eduardo Perez": [250000, 190000, 150000, 130000, 400000],
    "Jennifer Vargas": [400000, 270000, 300000, 150000, 450000],
    "Adolfo Jimenez": [90000, 180000, 70000, 100000, 250000]
}

print("=== REPORTE DE LOS TRABAJADORES ===")

#Iteramos por el diccionario 
for nombre in Vendedores:
    lista_ventas = Vendedores[nombre]
    #seguido de eso calculamos el numero de ventas total con un ciclo manual

    totaldeventas = 0
    for v in lista_ventas:
        totaldeventas = totaldeventas + v
    #Calculamos el promedio semanal, considerando que solo se cuentan 5 de los 7 dias de la semana
    PromedioVentas = totaldeventas / 5
    # tambien revisamos que bono corresponde segun lo obtenido en la venta semanal
    if totaldeventas > 1500000:
        porcentaje = 0.20
    elif totaldeventas > 1000000:
        porcentaje = 0.10
    elif totaldeventas > 500000:
        porcentaje = 0.05
    else:
        porcentaje = 0.0
        
    # Calcular el sueldo final
    bono_dinero = SueldoBase_2025 * porcentaje
    sueldo_final = SueldoBase_2025 + bono_dinero
    #Para terminar Mostramos los datos por terminal usando print
    print("----------------------------------------")
    print("Vendedor:", nombre)
    print("El Total de ventas semanales:", totaldeventas, "Pesos")
    print("El promedio de ventas diarias:", PromedioVentas, "Pesos")
    print("Bono recibido: ", bono_dinero, "(", porcentaje * 100, "%)")
    print("El total a pagar:", sueldo_final, "Pesos")