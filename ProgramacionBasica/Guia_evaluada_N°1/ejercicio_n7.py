from colorama import init, Fore
init()

dato = int(input("Ingrese un numero entero y positivo para saber su 'factorial': "))
print(f"\nEl valor ingresado es: {dato} \n")

factorial = 1
multiplicacion = ""

if dato >= 1:

    for itelal in range(dato, 0, -1):
        factorial = factorial * itelal
        multiplicacion = f"{multiplicacion}{itelal} * "
    print(f"{dato}! = {multiplicacion} = {factorial} \n")

elif dato == 0:
    print(Fore.BLUE + "El factorial de 0 es: 1 \n")
    
else: 
    print(Fore.RED + "Ingrese un valor entero y positivo \n")
