# lista, dicionario e set: mutaveis
def add(lista, item):
    lista.append(item)    #altera objeto

compras = ["arroz"]
add(compras, "feijao")
add(compras, 'ovo')
print(compras)  #['arroz', 'feijao']

# copia defensiva:protege o original
compras[1] = "cafe"
print(compras)