# Nombre = Maykol Coronado y Francisco Ojeda

conceptos_repetidos = ["inmutable", "iterable", "inmutable", "hashable", "interpretado", "iterable"]
conceptos_repetidos.sort()
print(conceptos_repetidos)

glosario = dict(
    Hashable = 'Objeto cuyo valor hash nunca cambia y puede ser clave',
    Inmutable = 'Objeto con un valor fijo que no se puede modificar',
    Interpretado = 'Lenguaje donde el código se ejecuta línea a línea',
    Iterable = 'Objeto capaz de devolver sus elementos uno a la vez'
)

buscar = str(input("Ingrese un concepto a buscar (hashable, inmutable, Interpretado, Iterable: "))
print(glosario[buscar])
