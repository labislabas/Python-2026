# Apuntes de variables
# Definicion de variables

"""
{estas son llaves}
(parentesis)
[corchetes]
"""

nombre = "Maykol"
apellido = "Coronado"
edad = 18

# Formas de immprimir texto

# Forma 1: Clásica separando variables y texto por comas
print ("Mi nombre es", nombre, "y mi apellido es", apellido, "y tengo", edad, "años")

#Forma 2: Utilizando f-strings
print(f"Mi nombre es {nombre} y mi apellido {apellido} y tengo {edad} años")

# Forma 3: Concatenación transforma un valor a texto
# La funcion str transforma 
print("Mi nombres es " + nombre + " y mi apellido es " + apellido " y tengo " + str(edad) + " años ") 

# Utilizando el método imput y creando una variable llamada carrera
carrera = input("¿Que carrera estudias?")
print(f"yo estudio la carrera de: {carrera}")

