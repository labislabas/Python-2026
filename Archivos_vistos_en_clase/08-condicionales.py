from colorama import init, Fore
init()   # INICIALIZANDO EL PAQUETE COLORAMA

print(Fore.RED +'\n===UTILIZANDO IF Y ELSE===')

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

license = False
edad = 19
automovil = True

if license and edad >= 18:
    print(Fore.YELLOW + "Puede conducir un automovil ya que es mayor de edad y tiene licencia")
elif automovil: 
    print("no puede conducir un automovil porque no es mayor de edad y no tiene licencia")

if license and edad >= 18:
    print(Fore.CYAN +"Puede conducir ya que es mayor de edad, y tiene licencia")
elif automovil:
    print(Fore.BLUE + "Tengo auntomivil pero no tengo ni licensia ni la edad suficiente para conducir")
else:
    print(Fore.RED + "No puede conducir ya que no tiene ni la edad suficiente, ni licencia, ni automovil")

    

