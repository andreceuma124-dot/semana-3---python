def perfil(**dados):
    #dados chega com DICIONARIO
    for chave, valor in dados.items():
        print(chave, ":", valor)

perfil(nome="Ana", idade=25, sexo="feminino",escolaridade="universitaria",mae="fernanda")
# nome : Ana
# idade : 25       

perfil(nome="joao", idade=34, sexo="masculino",escolaridade="universitario",mae="maria")