nome=input("informe o nome produto = ")
quant=float(input("Informe a quantidade comprada = "))
valorunitario=float(input("informe o valor unitario = "))
descontounitario=float(input("informe o valor do desconto = "))
vlt= (quant*valorunitario)-(quant*valorunitario*descontounitario/100)

print("o nome do produto é " ,nome,"\no  valor do desconto é " ,vlt , )
