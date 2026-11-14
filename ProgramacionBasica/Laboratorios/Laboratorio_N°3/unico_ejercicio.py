# A

print("===DICCIONARIO ANTIGUO===\n")
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

densidad_de_14 = round(censo_2017[14]["Habitantes"] / censo_2017[14]["Superficie"], 1)
densidad_de_12 = round(censo_2017[12]["Habitantes"] / censo_2017[12]["Superficie"], 1)

censo_2017[14]["densidad"] = densidad_de_14
censo_2017[12]["densidad"] = densidad_de_12

# C

censo_2017[14]["Capital"] = "Valdivia"
censo_2017[14]["Comunas"] = ["Rio Bueno", "La Union", "Paillaco"]
censo_2017[14]["Coordenadas_simuladas"] = (-39.8, -73.2)
censo_2017[14]["Zonas_exclusivas"] = {"Urbana", "Rural", "Fronteriza"}

censo_2017[12]["Capital"] = "Punta Arenas"
censo_2017[12]["Comunas"] = ["Cabo de Hornos", "Puerto Williams", "Porvenir"]
censo_2017[12]["Coordenadas_simuladas"] = (-59.9, -90.2)
censo_2017[12]["Zonas_exclusivas"] = {"Urbana", "Rural", "Fronteriza"}

# E

solicitud = int(input("\nIngrese el ID de la comuna a buscar (14 -> Los ríos) (12 -> Magallanes): \n"))

if solicitud == 14:
    print("Las comunas de Los Ríos son:", censo_2017[14]['Comunas'])
elif solicitud == 12:
    print("Las comunas de Magallanes son:", censo_2017[12]['Comunas'])
else:
    print(f"ID incorrecto, {solicitud}")

# F
print("\n===Diccionario nuevo===\n")
print(tuple(censo_2017.items()))