notas = {
    "Ana": 6.2,
    "Luis": 4.8,
    "Pedro": 3.9,
    "Sofía": 5.5
}

aprobados = 0

for nombre, nota in notas.items():
    if nota >= 4.0:
        print(f"{nombre} : {nota} -> Aprobado")
        aprobados += 1
    else:
        print(f"{nombre} : {nota} -> Reprobado")

print(f"Total de aprobados: {aprobados}")