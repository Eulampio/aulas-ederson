
saldo= 10.0

senha=1234 
digite=int(input("informe a senha :"))

if digite==senha:
    opcao=input("\ninforme qual opçao \nA se for Extrato\nB se for Deposito\nC se for Saque\nD Cadastro \nE se for sair\n Digite a Opçao: ")
    if opcao=="A" or opcao=="a":
        print("Seu saldo é de = ",saldo)
   
    elif opcao=="B" or opcao=="b":
        deposito=float(input("Informe o valor a ser depositado = "))
        saldo = deposito+saldo
        print("Seu saldo atual é de =" ,saldo)
  
    elif opcao== "C" or opcao=="c":
        saque=float(input("Informe o valor que deseja sacar = "))
        saldo= saldo-saque
        print("Seu saldo é de =" ,saldo)
    
    elif opcao=="D" or opcao== "d":
        print("Seu nome xxxxx CPF XXXX FONE XXXX SEXO XXX1234")
        nome= str(input("\nInforme o nome: "))
        cpf =int(input("informe seu CPF: "))
        fone = int(input("informe seu telefone: "))
        sexo = str(input(("informe seu sexo: ")))
        print("seu dados são Nome %s CPF %d Telefone %d Sexo %s"% (nome,cpf,fone,sexo))

   
    elif opcao=="E" or opcao== "e":
        print("seção encerrada")
    
   
    else:
        print("Opção invalida ")

    


else:
    print("senha invalida")

