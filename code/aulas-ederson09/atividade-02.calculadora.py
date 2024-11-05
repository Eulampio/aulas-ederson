while True:           
    try:

        n1=int(input("Digite 1 para adiçao\nDigite 2 para subtração\nDigite 3 para Divisão\nDigite 4 para Multiplicação\nInforme a opção: "))
        try:

            if n1==1:
                a=int(input("Informe o numero: "))
                b=int(input("Informe o numero: "))
                n1=a+b
                print("o resuldado é: ",n1)
            elif n1==2:
                a=int(input("Informe o numero: "))
                b=int(input("Informe o numero: "))
                n1=a-b
                print("o resuldado é: ",n1)
            elif n1==3:
                a=int(input("Informe o numero: "))
                b=int(input("Informe o numero: "))
                n1=a/b
                print("o resuldado é: ",n1)
            elif n1==4:
                a=int(input("Informe o numero: "))
                b=int(input("Informe o numero: "))
                n1=a*b
                print("o resuldado é: ",n1)
        
        except ZeroDivisionError:
            print("nao pode ser 0")
        
        
    except:
        print("digite apenas numero")