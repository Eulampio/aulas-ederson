cont=0
while True:
    while True:
        x=int(input("1-camisa 38,00\n2-short 35,00\n3-meia 10,00\n4-cueca 15,00\n5-casaco 75,00\n0-finalizar\n"))
        if x==1:
            y=int(input("dgt a quantidade"))
            cont=cont+38*y
            print(cont)
        elif x==2:
            y=int(input("dgt a quantidade"))
            cont=cont+35*y
            print(cont)
        elif x==3:
            y=int(input("dgt a quantidade"))
            cont=cont+10*y
            print(cont)
        elif x==4:
            y=int(input("dgt a quantidade"))
            cont=cont+15*y
            print(cont)
        elif x==5:
            y=int(input("dgt a quantidade"))
            cont=cont+75*y
            print(cont)
        elif x==0:
            break
        else:
            print("opção invalida")
    while True:

        print("o valor a ser pago e ",cont)
        a=int(input("dgt o valor do pagamento"))

        if a<cont:
            print("valor invalido")
        elif a>=cont:
            b=a-cont
            print("O troco e de ",b)
            break
        

    
            
        
















