# Miembros: Leonardo y Maykol
#Primero solicitamos ingresar el valor de n por terminal

# Miembros: [Nombre 1] y [Nombre 2]

# Solicitar el valor de n por teclado

n = int(input("Ingrese el número de cubos a calcular (n): "))

# Iniciar el primer número impar de la secuencia
impar = 1

# Bucle principal para controlar cada nivel (desde el cubo 1 hasta n)
for i in range(1, n + 1):
    suma_cubo = 0
    texto_impar = ""

    # Bucle interno: se ejecuta 'i' veces para sumar los números impares de este nivel
    for j in range(i):
        suma_cubo = suma_cubo + impar

        # Construimos el texto de la suma (por ejemplo, "7 + 9 + 11")
        if j == 0:
            texto_impar = str(impar)
        else:
            texto_impar = texto_impar + " + " + str(impar)

        # Pasar al siguiente número impar consecutivo
        impar = impar + 2

    # Imprimir la línea con el formato de la propiedad de Nicómaco
    print(str(i) + "^3 = " + texto_impar + " = " + str(suma_cubo))