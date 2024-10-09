#As maças custa R$ 0,30 cada se forem compradas menos do que uma duzia , e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o numero de maçãs compradas, e calcule e escreva o valor total da compra
maca = int(input("informe quantas maças estão sendo compradas: "))

if maca>=12:
  qtd=  maca*0.25
  print("o valor a ser pago",qtd)
elif maca<12:
  qtd=  maca*0.30
  print("o valor a ser pago",qtd)