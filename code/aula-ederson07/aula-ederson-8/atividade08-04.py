
#faça um programa que leia 5 numeros e informe a soma e a media dos números
# n=int(input("informe 1° numero: "))
# n2=int(input("informe 2° numero: "))
# n3=int(input("informe 3° numero: "))
# n4=int(input("informe 4° numero: "))
# n5=int(input("informe 5° numero: "))
# soma=n+n2+n3+n4+n5
# media=(n+n2+n3+n4+n5)/5
# print("O resultado da soma é %d e a madia dos numero é %d "% (soma,media))
numero2=0 #acumulador da soma
numero=5#contador para inserir os numeros 
for a in range(0,numero):
     numero=int(input("informe um numero: "))
     numero2=numero2+numero
     media=numero2/5
     print("O resultado da soma é %d e a madia dos numero é %d "% (numero2,media))
