while True:


    n1=int(input("informe a operação desejada (1) para Soma\n (2) para Subtração\n (3) pama Multiplicação \n(4) para Divisão \n(5) para sair"))
    if n1==1:
        a=float(input("digite o 1° valor"))
        b=float(input("digite o 2° valor"))
        c= a+b
        print("O resultado da soma é %.2f"%(c))


    elif n1==2:
        a=int(input("digite o 1° valor"))
        b=int(input("digite o 2° valor"))
        c= a-b
        print("O resultado da Subtração é %.2f"%(c))
    elif n1==3:
        a=int(input("digite o 1° valor"))
        b=int(input("digite o 2° valor"))
        c= a*b
        print("O resultado da Multiplicação é %.2f"%(c))
    elif n1==4:
        a=int(input("digite o 1° valor"))
        b=int(input("digite o 2° valor"))
        c= a/b
        print("O resultado da Divisão é %.2f"%(c))

    elif n1 ==5:
       print("saindo da tabuada")
       break
    else:
        print("opção invalida")
