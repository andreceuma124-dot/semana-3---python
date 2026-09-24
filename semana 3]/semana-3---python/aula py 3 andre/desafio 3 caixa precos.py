def caixa(*precos):
    """Retorna o total, o maior preço e a média dos preços."""
    total = sum(precos)
    mais_caro = max(precos)
    media = total / len(precos)

    return total, mais_caro, media


total, mais_caro, media = caixa(10, 25.5, 7)

print(f"Total: R$ {total:.2f}")
print(f"Item mais caro: R$ {mais_caro:.2f}")
print(f"Média: R$ {media:.2f}")