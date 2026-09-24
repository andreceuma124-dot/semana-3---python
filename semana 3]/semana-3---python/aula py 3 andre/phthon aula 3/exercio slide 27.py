def criar(nome, ativo=True):
    if ativo:
        s = "disponivel"
    else:
        s = "Esgotado"
    return nome + "-" + s

print(criar("Caneta"))  # Disponivel
print(criar("Caneta", False))