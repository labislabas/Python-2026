"""Al desarrollar sistemas informaticos, los usuarios suelen ingresar datos con espacios
accidentales o formatos incorrectos. El sistema de la biblioteca de la ULagos recibio el
RUT de un estudiante, pero viene “sucio” con espacios al inicio, al final y con puntos
intermedios: “ 19.543.872-K ”...
Escribe un programa que:
a) Guarde el RUT original en una variable de tipo string.
b) Utilice el metodo propio de Python para eliminar los espacios en blanco de los
extremos.
c) Utilice un metodo propio de Python para eliminar los puntos (.).
d ) Calcule el largo total del RUT ya limpio (sin espacios ni puntos) y muestre el
resultado por pantalla junto al RUT con su nuevo formato."""


rut = " 19.543.872-k "   #TIENE QUE QUEDAR: "19.543.872-K"

rut_sin_espacio = rut.strip()         #ELIMINA LOS ESPACIOS EXTREMOS

rut_final = rut_sin_espacio.replace(".","")      #ELIMINA LOS PUNTOS
print(rut_final)

largo_de_rut = len(rut_final)

print(f"Largo del rut: {largo_de_rut} | rut: {rut_final}")
