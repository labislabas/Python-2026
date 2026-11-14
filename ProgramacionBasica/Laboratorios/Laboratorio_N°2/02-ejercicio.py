codigo_identificador = input("Ingrese su codigo identificador: ")

codigo_identificador = codigo_identificador.strip()            # ELIMINA LOS ESPACIOS DE LOS EXTREMOS
codigo_identificador = codigo_identificador.replace("_","")    # REEMPLAZA LOS GUIONES BAJO POR 'NADA'
codigo_identificador = codigo_identificador.upper()            # IMPRIME LOS CARACTERES EN MAYUSCULA

largo_caracteres = len(codigo_identificador)                   # IMPRIME LA CANTIDAD DE CARACTERES DE LA VARIABLE 'CODIGO_IDENTIFICADOR'

print(f"Su codigo identificador 'limpio' es: {codigo_identificador} | La longitud de su codigo identificador es: {largo_caracteres}")