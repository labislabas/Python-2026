# Datos numericos

"""
int (enteros)
float (reales)
complex (complejos)
"""

# Números enteros
print("-------- NÚMEROS ENTEROS --------")

edad = 18
añonac = 2008

print(f"Actualmente tengo {edad} años, por lo que naci en el {añonac}")


# Números flotantes (Reales)    
#(El decimal se utiliza punto y no coma)
print("--------NÚMEROS FLOTANTES (REALES)--------")
estatura = 184.5
peso = 92.8

print(f"Yo mido {estatura} centimetros y peso {peso} kilogramos")


# Números complejos
print("-------- NÚMEROS COMPLEJOS --------")
num_complejo = 2 +3j             # Primera forma de crear un número complejo
otro_complejo = complex(4,2)     # Segunda forma de crear un número complejo


# Opreación aritmetica basica (Area de un triangulo) 
base = 8
altura = 12.5

area = (base * altura) /2

print(f"El área del tríangulo es de {area} cm")

PI = 3.1416
print(f"El valor de PI es aproximadamente {PI:.2f}")     # El formato :.2f limita el número de decimales a 2, redondeando el valor de PI a 3.14


# El método de redondeo 
print("-------- METODO DE REDONDEO --------")

print(round(area))
print(f"El area del trínagulo es de {round(area)} cm")

# Transformaciones de números
print(float(edad))


# CADENA DE TEXTOS (STRINGS)
print("-------- CADENA DE TEXTOS (STRINGS)--------")

carrera = "Ingenieria civil en informática"
institucion = "Universiadad de los lagos"
 
print(carrera[1])      # Imprime la posición del caracter en la cadena de texto (n), ya que la posición inicia en 0
print(carrera[-1])     # Imprime el último caracter de la cadena de texto (a), utilizando un índice negativo

print("hola" * 4)  # Multiplicaicon de una cadena de texto, repitiendo la palabra "hola" 4 veces

print(carrera[0:10])   # Imprime un rango de caracteres desde la posición 0 hasta la posición 9 (Ingenieria)

# Metodo len() permite conocer la cantidad de caracteres que tiene una cadena de texto (ademas de coontar los espacios)


# ARREGLOS (LISTAS)
print("---------- ARREGLOS (LISTAS) ----------")
colores = ["azul", "rojo", "verde", "amarillo"]  # Arreglo de stings
numeros = [1,2,3,4,5]                            # Arreglo númerico

print(colores[0])   # Imprime el primer elemento de la lista de colores (azul)  
print(numeros[-1])  # Imprime el último elemento de la lista  de números (5)

