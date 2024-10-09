#escreva um programa que verifique a validade de uma senha fornecida pelo Usuario . A senha é i numero  1234. Devem ser impressas as segintes mensagens
#ACESSO PERMITIDO caso a senha seja vadida
#ACESSO NEGADO caso a senha seja Inválida
senha = int(input("incira a Senha : "))

if senha != 1234:
    print=("ACESSO NÃO  PERMITIDO")
elif senha==1234:
        print("ACESSO PERMITITO")