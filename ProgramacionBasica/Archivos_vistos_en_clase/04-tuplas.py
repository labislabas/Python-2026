# TUPLAS

estudiantes = ("Matias", "Francisco", "Alan", "Maykol")
print(type(estudiantes))
print(f"Tupla: {estudiantes}")


# CREANDO UNA TUPLA COMPLEJA CON DATOS ESTRUCTURADOS
datos = ([1,2,3,4], ("Queilen", "Castro"), ("Universidad de los Lagos", "AIEP"))


# TAMBIEN SE PUEDE CONSULTAR LA POSICION DE UN ELEMENTO AL IGUAL QUE LA LISTA
print(datos[0])
print(f"TUPLA: {datos}")


# CON LAS LISTAS SE PUEDE ELIMINAR LOS ELEMENTOS
lista_asignaturas = ['Programacion', 'Quimica', 'Introduccion a la matematicas']
print(f"LISTAS: {lista_asignaturas}")

lista_asignaturas.pop()
print(f"LISTA SIN ÚLTIMO ELEMENTO: {lista_asignaturas}")

# ¿ QUE PASA SI QUIERO ELIMINAR EL ULTIMO ELEMENTO DE UNA TUPLA
"""estudiantes.pop()
print(f"TUPLA CON ULTIMO ELEMENTO ELIMINADO: {estudiantes}")"""


# OCUPAREMOS EL METODO INDEX PARA CONSULTAR LA POSICION DE UN ELEMENTO
print(estudiantes.index('Alan'))    # SE ENCUENTRA EN LA POSICION 2


# METODO SORTED() PARA ORDENAR ELEMENTOS DE UNA TUPLA
print(sorted(estudiantes))
