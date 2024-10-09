uma_lista=["a","b","c","d","e","f"]
print(uma_lista)
print(len(uma_lista))
uma_lista[1:3]=[]
print(uma_lista)
print(len(uma_lista))
#inserir na lista
uma_lista01=["a","d","f"]
uma_lista01[4:4]=["e"]
uma_lista01[1:1]=["b","c"]
print(uma_lista01)
#remover o item de uma lista
a=["um","dois","tres"]
del a[1]
print(a)
uma_lista02=["a","b","c","d","e","f"]
del uma_lista02[1:5]
print(uma_lista02)
#operador ponnto metodo nativo para inserir elementos na lista
b= [81,82,83]
b.append(5)
print(b)
#ordernar numeros do mair para o menor (reverse=True)
c=[88,81,82,83]
c.sort()
print(c)
d=[88,81,82,83]
d.sort(reverse=True)
print(d)
#adicionar elemento index
e=[1,2,3,4,5,6,7,8,9,10]
print(e.index(4))
f=[88,81,82,83]
f.insert(3,100)
print(f)
# count para ver quantas vezes um elemento aparece na lista
g=[1,2,3,4,5,6,7,8,9,10,1,1,1,1,]
print(g)
print(g.count(1))
#apagar o ultimo elemento ou remover tambem
h=[1,2,3,4,5,6,7,8,9,10,1,1,1,1,]
h.pop
print(h)
a.pop(0)
print(h)
#adicionar lista dentro de lista extrnde
listao1 = [1,2,3]
listao1.extend([4,5])
print(listao1)