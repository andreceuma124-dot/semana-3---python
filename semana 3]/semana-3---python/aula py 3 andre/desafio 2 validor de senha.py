
def senha_valida(senha):
    """Retorna True se a senha tiver 8 ou mais caracteres."""
    return len(senha) >= 8


senha = input("Digite a senha:124356789 ")
print(senha_valida(senha))
