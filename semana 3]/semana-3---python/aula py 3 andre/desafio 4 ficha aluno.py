def ficha_aluno(**dados):
    """Imprime as informações do aluno, uma por linha."""
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


ficha_aluno(
    nome="Andre",
    idade=18,
    curso="Programação",
    nota=8.5
)
