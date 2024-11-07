def cadastro():
    nome= input("Qual seu nome: ")
    age=int(input("idade: "))
    return nome,age
print("iniciano Cadastro")
nome,idade= cadastro()
print("Cadastor realizado com sucesso")
print("Seu nome é ",nome,"e voçê tem " ,idade,"anos")