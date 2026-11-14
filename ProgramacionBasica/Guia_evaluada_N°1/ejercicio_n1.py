# Miembros: Leonardo y Maykol
# Primero, ingresamos el siguiente párrafo a través del terminal

# El Proyecto Integrador del primer semestre será evaluado y desarrollado en 3 materias juntas: Taller de Introducción a la Ingeniería, donde trabajarán en el desarrollo práctico del proyecto, Habilidades de Comunicación, donde desarrollarán habilidades de presentación y escritura, y finalmente Programación, donde aplicarán técnicas para codificar y diseñar el software del proyecto

Parrafo = input("Ingrese el párrafo:")

# Verificamos si el texto está vacío comparándolo con un texto vacío:

if Parrafo == "":
    raise ValueError("El texto ingresado no puede estar vacío, por favor intente de nuevo")

# Limpiamos el texto eliminando puntos y comas para que no se peguen a las palabras al separarlas
# para hacer la lista:

Parrafo = Parrafo.replace(".", "")
Parrafo = Parrafo.replace(",", "")
Parrafo = Parrafo.replace(":", "")

# Separamos el texto para poder guardarlo en una lista y pasarlo a una tupla

ListaPalabras = Parrafo.split()
Tupla_Palabras = tuple(ListaPalabras)

# Ahora solicitamos una palabra para buscar

PalabraBuscar = input("Ingrese la palabra a buscar, considere que puede ser sensible a mayúsculas:")

# Continuamos contando cuántas veces aparece la palabra en el texto ingresado y luego imprimimos el resultado
# en la consola

Conteo_Palabra = Tupla_Palabras.count(PalabraBuscar)

print("La palabra a buscar aparece:", Conteo_Palabra, "veces")