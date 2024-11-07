def inverte(nome, sobrenome):
    nomeInveso = sobrenome +","+ nome
    return nomeInveso
nome=input("Nome: ")
sobrenome = input("Sobrenome: ")
invertido=inverte(nome, sobrenome)
print("OLÁ ", invertido)