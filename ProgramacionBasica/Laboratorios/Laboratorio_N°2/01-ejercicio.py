# TRANSFORMAR LOS DATOS INGRESADOS EN FLOAT/DECIMALES

primera_muestra = float(input("Ingrese la primera muestra meteorologica: "))
print(primera_muestra)                                                       

segunda_muestra = float(input("Ingrese la segunda muestra meteorologica: "))
print(segunda_muestra)

tercera_muestra = float(input("Ingrese la tercera muestra meteorologica: "))        
print(tercera_muestra)

cuarta_muestra = float(input("Ingrese la cuarta muestra meteorologica: "))
print(cuarta_muestra)

quinta_muestra = float(input("Ingrese la quinta muestra meteorologica: "))
print(quinta_muestra)


registro_lluvia = [primera_muestra, segunda_muestra, tercera_muestra, cuarta_muestra, quinta_muestra]  


promedio_precipitaciones = (registro_lluvia [0] + registro_lluvia [1] + registro_lluvia [2] + registro_lluvia [3] + registro_lluvia [4]) / 5


brecha_pluvial = max(registro_lluvia) - min(registro_lluvia)


print(f"Lista completa de datos (todo esto en milimetros): {registro_lluvia} | Promedio de los datos: {promedio_precipitaciones} mm | Brecha pluvial de la tormenta: {brecha_pluvial} mm")