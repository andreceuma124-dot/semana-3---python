
def adicionar_item(lista, item):
    """Adiciona um item a uma cópia sem alterar a lista original."""
    nova_lista = lista[:]
    nova_lista.append(item)
    return nova_lista


notas = [7, 8]

nova_lista = adicionar_item(notas, 9)

print(f"Nova lista: {nova_lista}")
print(f"Lista original: {notas}")
