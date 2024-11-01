#resolver bug
total=0
troco=0
while True:
    valor= float(input(" informe o valor do produto ou zero (0)  para parar: "))
    mercadoria= str(input("informe o produdo: "))
    total=total+valor
    produto= mercadoria+mercadoria
    print(total)
    print(produto,",")
    if valor==0:
        break
while True:
    print("total das conpras é : ",total)

    dinhero=float(input("informe o dinhero"))
    
    
    if dinhero<total:
        print("valor insuficiente")

    elif dinhero>=valor:
        troco=dinhero-total
        break
print(troco,mercadoria)


    


        
        
       
    

       
    