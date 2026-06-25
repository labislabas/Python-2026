tablero = {}
columnas = ["a", "b", "c", "d", "e", "f", "g", "h"]
piezas_principales = ["Torre", "Caballo", "Alfil", "Reina", "Rey", "Alfil", "Caballo", "Torre"]

for i in range(8):
    for fila in [1, 2, 7, 8]:
        if fila == 1:
            tablero[columnas[i] + "1"] = piezas_principales[i] + "B"
        elif fila == 2:
            tablero[columnas[i] + "2"] = "PeonB"
        elif fila == 7:
            tablero[columnas[i] + "7"] = "PeonN"
        elif fila == 8:
            tablero[columnas[i] + "8"] = piezas_principales[i] + "N"

simbolos = dict(
    TorreB = 'R',
    ReinaB = 'Q',
    TorreN = 'r',
    ReinaN = 'q',
    CaballoB = 'N',
    ReyB = 'K',
    CaballoN = 'n',
    ReyN = 'k',
    AlfilB = 'B',
    PeonB = 'P',
    AlfilN = 'b',
    PeonN = 'p'
)

capturadas = []

print("=== SIMULADOR DE AJEDREZ ===")


print("\n  a b c d e f g h")
for fila in range(8, 0, -1):
    linea = str(fila) + " "
    for i in range(8):
        casilla = columnas[i] + str(fila)
        if casilla in tablero:
            linea = linea + simbolos[tablero[casilla]] + " "
        else:
            linea = linea + ". "
    linea = linea + str(fila)
    print(linea)
print("  a b c d e f g h")

while True:

    origen = input("\nIngrese casilla de origen: ")
    destino = input("Ingrese casilla de destino: ")

    if origen not in tablero:
        print("Error: No existe ninguna pieza en esa casilla.")
        continue

    pieza_origen = tablero[origen]

    if destino in tablero:
        pieza_destino = tablero[destino]

        if pieza_origen[-1] == pieza_destino[-1]:
            print("Error: Ya hay una pieza tuya en esa casilla.")
            continue

        capturadas.append(pieza_destino)
        print("Capturó a", pieza_destino, "en", destino)

    tablero[destino] = pieza_origen
    del tablero[origen]

    print("\n  a b c d e f g h")
    for fila in range(8, 0, -1):
        linea = str(fila) + " "
        for i in range(8):
            casilla = columnas[i] + str(fila)
            if casilla in tablero:
                linea = linea + simbolos[tablero[casilla]] + " "
            else:
                linea = linea + ". "
        linea = linea + str(fila)
        print(linea)
    print("  a b c d e f g h")
    print("Capturadas:", capturadas)