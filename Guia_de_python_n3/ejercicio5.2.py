"""Una plataforma web de la Universidad de Los Lagos mide la velocidad de respuesta
de su servidor de asignacion de asignaturas. Se han tomado 3 muestras de tiempo de
respuesta (en milisegundos) de forma manual. Escribe un programa en Python que:
a) Solicite al administrador de la plataforma ingresar por terminal los 3 tiempos de
respuesta (los cuales pueden contener decimales, tipo float).
b) Almacene los 3 valores ingresados dentro de una lista de Python que debe tener
por nombre tiempos respuesta.
c) Acceda por medio de sus ındices ([0], [1], [2]) a los elementos de la lista para
calcular el tiempo promedio de respuesta del servidor.
d ) Encuentre el tiempo mas rapido (minimo) y el tiempo mas lento (maximo) utili-
zando las funciones propias de Python.
e) Calcule la “brecha de rendimiento”, que corresponde a la resta entre el tiempo
maximo y el minimo.
f ) Imprima en pantalla la lista completa de datos y el reporte con el promedio y la
brecha calculada."""

toma_tiempo1 = float(input("Adminitrasdos ingrese le tiempo de respuesta numero 1: "))
toma_tiempo2 = float(input("Adminitrasdos ingrese le tiempo de respuesta numero 2: "))
toma_tiempo3 = float(input("Adminitrasdos ingrese le tiempo de respuesta numero 3: "))

tiempos_respuetas = []
tiempos_respuetas.append(toma_tiempo1)
tiempos_respuetas.append(toma_tiempo2)
tiempos_respuetas.append(toma_tiempo3)
print(tiempos_respuetas)

promedio_tiempos = (tiempos_respuetas [0] + tiempos_respuetas [1] + tiempos_respuetas [2]) /len(tiempos_respuetas)

min_tiempo = min(tiempos_respuetas)  # MAS RAPIDO
max_tiempo = max(tiempos_respuetas)  # MAS LENTO

brecha_tiempo = (max_tiempo - min_tiempo)

print(f"A continuacion la listas completa de los tiempo de respuesta y datos: \n Tiempos de respuestas: {tiempos_respuetas} \n Promedio: {promedio_tiempos} \n Brecha de tiempo: {brecha_tiempo}")

