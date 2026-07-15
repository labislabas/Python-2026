# Nombre = Maykol Coronado y Francisco Ojeda

conceptos_repetidos = ["inmutable", "iterable", "inmutable", "hashable", "interpretado", "iterable"]
conceptos_repetidos.sort(key=len)
print(set(conceptos_repetidos))

glosario = dict(
    hashable = 'Objeto cuyo valor hash nunca cambia y puede ser clave',
    inmutable = 'Objeto con un valor fijo que no se puede modificar',
    interpretado = 'Lenguaje donde el código se ejecuta línea a línea',
    iterable = 'Objeto capaz de devolver sus elementos uno a la vez'
)

buscar = str(input("Ingrese un concepto a buscar (hashable, inmutable, interpretado, iterable: "))

definicion = glosario[buscar]
print(f"{buscar}: {definicion}")
 
registro_busqueda = (buscar, definicion)
print(registro_busqueda)