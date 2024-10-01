a="ederson"
b="EDERSON"
c="12345"
d="123abc"
e="alexandre da silva santos"
f="alexandre-da-silva-santos"
print(a.capitalize())
print(len(a)) #conta os numero de string
print(a.upper())#upper para maiusculo
print(b.casefold())
print("ALEXANDRE".upper())
print(b.lower())#lower tranforma em minuscula
print(b.islower())#islower esta tudo minuscolo
print(b.isupper())#isupper identifica se o texto esta em maiúsculo
print(c.isdigit())#isdigit como verificar string so possui numeros inteiros
print(d.isdigit())
print(e.replace("santos","eulampio"))#replace o metodo replace serve para trocar todos a ocorrescia de uma substring outra em uma string
print(f.split("-"))#split(sep) separa a string usando sep  como separador.retorna uma lista das substrings. se passando sem parâmetro substintuindo o espaço por ","(virgula)ou parametro por "," (virgula)
print(e.find("santos"))# find metodo retorna onde a substring começa string 
print("santos" in e)# in o operador in verifica se uma substring e parte de uma outra string
print(e.count("a"))#count o operado retorna a frequência do parametro passado
print(e[19])#imprime as string na posição indicada
print(e[-20])
print(e[0:9])
print(e[:9])#entende como zero (0)