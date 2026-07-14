# A

print("===DICCIONARIO ANTIGUO===")
censo_2017 = {
    14 : {
        'Nombre Región' : 'Los Ríos',
        'Superficie' : 18.429,
        'Habitantes' : 404.432
    },
    
    12 : {
        'Nombre Región' : 'Magallanes',
        'Superficie' : 1.382291,
        'Habitantes' : 166.533
    }
}

print(censo_2017)

# B

densidad = 404.432 / 18.429
densidad_2 = 166.533 / 1.382291

censo_2017[14].update(densidad = '21.9')
censo_2017[12].update(densidad = '120.4')

# C

censo_2017[14].update(Capital = 'Valdivia')
censo_2017[14].update(Comunas = {
    'Río bueno, La Unión, Paillaco'
})

# SE INTENTO AGREGAR UNA TUPLA Y SET

#censo_2017[14].update(tuple(latitud_longitud = 45.6_79))
#censo_2017[14].update(set(Zonas_esclusivas = 'Urbano, Peligroso, Inseguro'))

censo_2017[12].update(Capital = 'Punta arenas')
censo_2017[12].update(Comunas = {
    'Cabo de hornos, Puerto Williams, Porvenir'
})

print(censo_2017)

# SE INTENTO AGREGAR UNA TUPLA Y SET

#censo_2017[12].update(tuple(latitud_longitud = 25.6_29))
#censo_2017[12].update(set(Zonas_esclusivas = 'Rural, Seguro, Frio'))

# D

censo_2017[12]

# E

solicitud = int(input("Ingrese el ID de la comuna a buscar (14 -> Los ríos) (12 -> Magallanes): "))

if solicitud == 14:
    print(censo_2017)
elif solicitud == 12:
    print("Las comunas de Magallanes son: Cabo de hornos, Puerto Williams, Porvenir")
else:
    print(f"ID incorrecto, {solicitud}")

# F
print("===Diccionario nuevo===")
print(tuple(censo_2017))