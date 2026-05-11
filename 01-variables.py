# Apuntes de variables
# Definicion de variables

"""
{estas son llaves}
(parentesis)
[corchetes]
"""


# Formas de imprimir texto

# Forma 1: # Apuntes de variables
# Definicion de variables

nombre = "Maykol"
apellido = "Coronado"
edad = "18"

# Formas de imprimir texto

# Forma 1: Utilizando el separador de la coma
print("Mi nombre es", nombre , apellido , "y tengo" , edad , "años")

# Forma 2: Utilizando f-strings
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

#Forma 3: Concatenación transforma un valor a texto
print("Mi nombre es " + nombre + " " + apellido + " y tengo " + edad + " años")
                

# Utilizando el metodo input y utilizando una variable carrera
carrera = input("¿Que carrera estudias?")
print(f"Yo estudio la carrera de:{carrera}")
                