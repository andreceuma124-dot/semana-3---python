# Imutáveis: números, strings, etc.
def muda(x):
    x = 10  # Só muda o nome local


n = 5
muda(n)

print(n)
# 5 -> não mudou


# Mutáveis: lista, dicionário, set
def inclui(lst):
    lst.append(4)  # Altera o objeto


v = [1, 2, 3]
inclui(v)

print(v)
# [1, 2, 3, 4]