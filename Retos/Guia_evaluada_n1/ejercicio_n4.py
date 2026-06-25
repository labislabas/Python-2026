n = int(input("Ingrese el numero de cubos a calcular (n): "))

impar = 1

for i in range(1, n + 1):
    suma_cubo = 0
    texto_impar = ""

    for j in range(i):
        suma_cubo = suma_cubo + impar

        if j == 0:
            texto_impar = str(impar)
        else:
            texto_impar = texto_impar + " + " + str(impar)

        impar = impar + 2

    print(str(i) + "^3 = " + texto_impar + " = " + str(suma_cubo))