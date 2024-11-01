#faça um programa que leia um valor em reais e caucule o valor equivalente em dolares. o usuario deve informar, alem do valor em reais da compra o valor da cotaçao em dolar
reais=float(input("informe o valor em reais = "))
cotaçao=float(input("informe a cotação do dolar ="))
valEmDolar=(reais*cotaçao )
print(f"o valor em reais é  {valEmDolar:..2f}")