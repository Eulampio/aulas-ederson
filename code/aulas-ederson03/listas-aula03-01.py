
#criando lista

lista=["ederson",37,1.75,80] 
print(lista)

lista1= [10,20,30,40]
lista2 = ["spam" ,"bungee","swollow"]
print (lista1,lista2) #varias lista 
#listas dentro de outra lista
lista3 = ["oi", 2.0 , 5, [10,20]]
print(lista3)
#o len não retorna a quantidade de intem
lista4=["oi", 2.0,5,[10,20]]
print(len(lista4))
#acessar o elementos das lista
numero= [17,123,87,34,66,8398,44]
print(numero[2])
print(numero[9-8])
print(numero[-2])
print(numero[-1])
#teste de entendimento
uma_lista=[3,67,"gato",[56,57,"cachorro"],[],3.14,False]
print(uma_lista[2][0])
#identificar se tem um elemento dentro de uma lista
frutas=["maca","laranja","banana","cereja"]
print("maca" in frutas)
print("pera" in frutas)
#concatenar lista[]
frutas1=["maca","laranja","banana","cereja"]
print([1,2]+[3,4])
print(frutas +[6,7,8,9])
print([]*4)
print([1,2,["ola","adeus"]]*2)
#menor valor e meno valor]
a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a))
c=["a","b","c"]
print(max(c))
#fatiar as strigs ou uma lista
uma_linta1=["a","b","c","d","e","f","g"]
print(uma_linta1[1:3])
print(uma_linta1[:4])
print(uma_linta1[3:])
print(uma_linta1[:])
print(uma_linta1[0:6])