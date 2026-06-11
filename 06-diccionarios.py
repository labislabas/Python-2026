# DICCIONARIOS 

paciente = {
    'nombre' : 'Benjamin Bahamonde',
    'edad' : 18,
    'ciudad' : 'Ancud',
    'Fechas_atencion' : [5,8,12],
    'diagnostico' : ('resfrio comun'),
    'Informacion_extra' : {   # CREACION DE UN SUB-DICCIONARIO
        'tipo_de_sangre' : 'A+',
        'Hemograma' : False
    }
}

# SEGUNDA FORMA DE DECLARAR UN DICCIONARIO 

medico = dict(
    nombre = 'Igancio Saez',
    edad = 19,
    especialidad = 'Cardiologo'
)

print(type(paciente))

print(f"=== FICHA PACIENTE === \n {paciente}\n")
print(f"=== FICHA PACIENTE === \n {medico}")

# CONSULTA DE DE INFORMACION A DICCIONARIOS

# ¿COMO CONSULTO EL NOMBRE DE UN PACIENTE SIN TRAER EL DICCIONARIO COMPLETO?
print(paciente['nombre'])

# A DIFERENCIA DE [], ESTE METODO NO GENERA ERROR SI NO EXISTE LA CLAVE
# METODO GET() OBTIENE EL VALOR DE UNA CLAVE, SI NO EXISTE RETORNA NONE (O UN VALOR POR DEFECTO EN VEZ DE UN ERROR)
print(paciente.get('nombre'))
print(paciente.get('rut', 'N/D (No Data'))

# RETONAR LAS CLAVES, LOS VALORES O AMBAS COMO PARES

print(paciente.keys())    # DICT_KEYS(['nombre', 'edad' ...]) -> SOLO CLAVES
print(paciente.values())  # DICT_VALUES(['Benjamnin', '18' ...]) -> SOLO VALORES
print(paciente.items())   # DICT_ITEMS([('nombre', 'Benjamin), ...]) -> POR CLAVE-VALOR -> LISTAS

print(len(medico))
print(len(medico))

# MODIFICACION DEL DICCIONARIO
# AGREGAR UNA CLAVE NUEVA AL DICCIONARIO PACIENTE

paciente['telefono'] = '+56987346134'

print("=== FICHA PACIENTE CON TELEFONO === \n")
print(paciente)

# SOBRESCRIBIR Y/O VALOR DE UNA CLAVE EXISTENTE (FORMA N°1)
paciente['edad'] = 20

print("=== FICHA PACIENTE CON EDAD ACTUALIZADA === \n")
print(paciente)

# FUSIONA OTRO DICCIONARIO (O PARES CLAVE-VALOR) EN EL ACTUAL 
# UTIL PARA ACTUALIZAR VARIOS CAMPOS A LA VEZ (ACTUALIZAR VARIAS CLAVES)
paciente.update({'edad' : 21, 'ciudad': 'Castro'})

print(paciente['edad'])
print(paciente['ciudad'])
print(paciente)

# ELIMINAR UNA CLAVE SIN RETORNO
del(paciente['Informacion_extra'])
print(paciente)

# ELIMINAR UNA CLAVE Y RETORNAR SU VALOR (A DIFERENCIA DE DEL, QUE NO LO RETORNA) -> POP()
edad_eliminada = paciente.pop('edad')
print(f'Edad eliminada: {edad_eliminada}')   # SE RECUPERA EL VALOR ANTES DE BORRARLA
print(paciente)

# OTRAS UTILIDADES DEL DICCIONARIO

# CON IN SE VERIFICA SI UNA CLAVE EXISTE EN EL DICCIONARIO (SIN USAR CONDICIONALES TODAVIA)
print('nombre' in paciente)
print('rut' in paciente)

# CON COPY() SE CREA UNA COPIA INDEPENDIENTE DEL DICCIONARIO
paciente2 = paciente.copy
paciente2['nombre'] = 'Javiera'
print(paciente['nombre'])
print(paciente2['nombre'])
print(paciente2)

# CON CLEAR() ELIMINA TODOS LOS ELEMENTOS DEL DICCIONARIO, DEJANDOLO VACIO (A DIFERENCIA DEL )
medico2 = medico.copy
print("\n === DICCIONARIO COPIA (MEDICO2) === \n ")
print(medico2)
medico2.clear()
print(medico2)   # -> {}