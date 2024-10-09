#teste codicional 
idade = int(input("Digite sua idade :"))
if idade==16: #caso verdadeiro
    print("pode votar")
else:
    if idade >=16:
        print("pode Dirigir")
    else:
        if idade< 16:
            print("Apenas estude")