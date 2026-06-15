alumno = {
    'nombre' : 'Benjamin',
    'edad' : '20'
}

# VERIFICANDO LA EXISTENCIA DE UN DATO/VARIABLE
if "nombre1" in alumno:     # SI (IF) NOMBRE1 EXISTE EN (IN) ALUMNOS  ENTONCES (:) SE EJECUTA 'EXISTE'
    print("Existe")
elif "edad1" in alumno:     # SINO (ELIF) SE CUMPLIO DE ARRIBA, PERO 'EDAD1' EXISTE EN (IN) ALUMNO ENTONCES (:) SE EJECUTA 'EXISTE'
    print("Existe.")
else:                       # SINO SE CUMPLIO NI 'IF' NI 'ELIF' ENTONCES (:) SE EJECUTA 'NO EXISTE NINGUNO'
    print("No existe ninguno")


estado = True
while estado == True:       # WHILE -> MIENTRAS
    respuesta = str(input("Usuario desea agregar un estudiante la diccionario 'estudiantes'?: (S/N)"))
    if respuesta == "S": 
        estudiante_agregar = str(input("Ingrese el nombre que desea agregar: "))
        edad = int(input("Ingrese la edad"))
    elif respuesta == "N":
        print("Entendido, Adios")
        estado == False
    else:
        print("La opcion idicada no es correcta, recuerde escribir 'S' para si o 'N' para no")

    

