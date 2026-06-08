# LISTAS

#PRIMERA FORMA DE DECLARARCIÓN DE LISTA 
lista1 = ["Victor", 32, True, "Victor", "Victor", "Victor"]
ramos = [] # LISTA VACIA

#SEGUNDA FORMA DE DECLARACIÓN DE LISTA (LISTA NÚMERICA)
n = list([5,4,3,2,1])

# METODOS PARA LAS LISTAS

#SE IMPRIME EL PRIMER ELEMNTO DE LA LISTA1 (VICTOR)
print(lista1[0])  

# 01 - CONT() CONTAR LA CANTIDAD DE CONCURRENCIAS DE UN ELEMENTO
print(lista1.count("Victor"))

print(ramos)

# AGREAGAR UN ELEMENTO AL FINAL DE LA LISTA
ramos.append('Química')
print(ramos)

ramos.append('Habilidades Comunuicativas')
print(ramos)

ramos.append('Programación')
print(ramos)

# OTRA FORMA DE INSERTAR UN ELEMENTO A LA LISTA (DE FORMA ESPECÍFICA)
ramos.insert(0, 'Habilidades Comunicativas para Ingenieros/as')
print(ramos)

# MODIFICAR UN ELEMNETO EN ESPECÍFICO DE UNA LISTA
ramos[2] = 'Hadbilidades Comunicativas para Ingenieros/as'
print(ramos)

#ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
ramos.pop()
print(ramos)

# ORDENA LOS ELEMENTOS DE UNA LISTA DE FORMA DESCENDENTE A ASCENDENTE
#print(ramos.sort())
ramos.sort()
print(ramos)

n.sort()
print(n)

# ORDENAR ELEMENTO DE UNA LISTA SEGÚN LA CANTIDAD DE CARACTERES DE CADA ELEMENTO
ramos.sort(key=len)
print(ramos)

# EXTENDER UNA LISTA A PARTIR DE OTRA
ramos_segundo_semestre = ['Ciudadanía', 'Álgebra', 'Introducción a la Física']

ramos.extend(ramos_segundo_semestre)
print(ramos)

# APLICANDO METODO INDEX
print(ramos_segundo_semestre.index('Algebra'))  # POSICION 1 
