total=0
dinhero=0

while True:
    valor= int(input(" informe o valor do produto ou zero (0)  para parar: "))
    total=total+valor
    print(total)
    if valor==0:
        break
    elif dinhero<valor:
        dinhero=int(input("informe o dinhero: "))
        print("valor insuficiente")
    elif dinhero>=valor:
        print("total das conpras é : ",total)

        
        
       
    

       
    