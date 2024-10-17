

while True:

    nome=str(input("Informe o nome:"))
    if len(nome) >3:
        print("%s"%(nome))
        break
    else:
        print("opção ivalida")
while True:
    idade=int(input("Informe a idade: "))
    if idade >=0 and idade<=150:
        print("%d"%(idade))
        break
    else:
        print("opção invalida")
while True:
     
    salario=int(input("informe o salario: "))
    if salario >=0:
       print("%d"%(salario))
       break

    else:
     print("opção invalida")
while True:
    sexo=str(input("informe o sexo sendo F para mulhe M para homem e (O) para refazer: "))
    if sexo=="o" or sexo=="m" or sexo=="o":
        print("%s"%(sexo))
        break
    else:
     print("opção invalida")


