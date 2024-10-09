#escreva um programa para ler o ano de nascimento de uma pessoa e escreva uma mensagem que diga se ele podera ou não votar este ano (não becessario considerar o mês em que ela nasce)
ano= int(input("inorme o ano de seu nascimento : "))
idade = 2024-ano
# print (idade)
if idade >=16:
    print("Ja pode votar")
elif idade < 16:
    print("Não pode votar")
