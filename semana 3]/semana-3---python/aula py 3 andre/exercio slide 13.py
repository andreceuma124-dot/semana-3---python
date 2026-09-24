# Procedimento com parâmetros
def cabecalho(titulo, largura=30):
    print(titulo.center(largura))
    print("-" * largura)


cabecalho("RELATORIO")

# Erro comum:
x = cabecalho("A") + 1 #Type Error