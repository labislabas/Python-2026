productos = [
"Pan", "Leche", "Pan",
"Queso", "Leche",
"Jugo", "Pan"
]

cantidad = len(productos)
print(f"Cantidad total de registros: {cantidad}")

productos_set = set(productos)

print("Productos distintos:")
for i in productos_set:
    print(i)

if 'Jugo' in productos:
    print('El producto Jugo fue vendido.')