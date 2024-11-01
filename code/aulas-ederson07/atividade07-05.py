

while True:

    nome=str(input("Informe o nome:"))
    if len(nome) >3:
        print("O nome informado foi : %s\n"%(nome))
    
        break
    else:
        print("opção ivalida")
while True:
    idade=int(input("Informe a idade: "))
    if idade >=0 and idade<=150:
        print("A idade informada foi: %d\n"%(idade))

        break
    else:
        print("opção invalida")
while True:
     
    salario=int(input("informe o salario: "))
    if salario >=0:
       print("O salario informado foi %d\n"%(salario))
       break

    else:
     print("opção invalida")
while True:
    sexo=str(input("informe o sexo sendo F para mulhe M para homem e (O) para refazer: "))
    if sexo=="o" or sexo=="m" or sexo=="c":
        print("O sexo informado foi : %s\n"%(sexo))
        break
    else:
     print("opção invalida")


