#faça um programa para a leitura de duas notas parciais de um aluno.  o programa deve calcular a media alcançada por aluno apresentae 
# A mendagem "Aprovado " se a media alcançada form maior que ou igual a sete
# A mensagem "Reprovado " se a média for menor do que sete
# A 
n1=float(input("informe a nota "))
n2=float (input("informe a nota "))

media = (n1+n2)/2
if media <7:
    print ("reprovado com a media %d"%(media))
elif media == 10:
     print("Aprovado com Didtição")
elif media >7 :
     print("aprovado com a media: %d"%(media) )