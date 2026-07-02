print("===MENU===")
print("1. Hamburgesa")
print("2. Pizza")
print("3. Completo italiano")

opcion = input("Por favor, elige una opcion (1-3): ")

match opcion:
    case "1": 
        print("Has eligido una Hamburgesa. Precio: $ 5.000")
    case "2":
        print("Has eligido Pizza. precio: $ 7.500")
    case "3":
        print("Has eligido Comleto italiano. $ 2.500")
    case _:
        print("Opcion no valida. Por favor, elige entre 1 y 3")

mes = 4
match mes: 
    case 12 | 1 | 2:
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 |7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("Mes invalido")

hora = 18
match hora: 
    case h if 0 <= h < 6:
        print("Buenas madrugadas")
    case h if 6 <= h < 12:
        print("Buenos dias")
    case h if 12 <= h < 18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("Hora invalida")

x = [1, 2, 3]
match x: 
    case [a, b, c]:     # DESAGRUPANDO VALORES DE LA LISTA X
        print(f"Elementos de la lista x: {a}, {b}, {c}")

datos = dict(
    nombre = 'Victor',
    edad = 31
)

match datos: 
    case {'nombre': n, 'edad': e}: 
        print(f"Nombre: {n}, Edad: {e}")

valor = input("Ingrese un numero entero para saber si es par o impar")
match valor: 
    case x if x % 2 == 0:       # MATCH TOMA EL VALOR DE CUALQUIER VALOR
        print(f"{valor} es un numeor Par")
    case x if x % 2 != 0:
        print(f"{valor} es un numeor Impar")
