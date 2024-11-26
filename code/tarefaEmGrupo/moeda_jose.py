import matplotlib.pyplot as plt
x=[1,2,3,4]# valor de x
y=[1,4,9,16] #valor de y
plt.plot(x,y,label= "Crescimeno")
plt.title("grafico simples")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.legend()
plt.show

import matplotlib.pyplot as plt
x=[1,2,3,4,5]# valor de x
y=[2,4,9,16,25] #valor de y
plt.plot(x,y,label= "Crescimeno")
plt.title("grafico simples")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.legend()
plt.show

import matplotlib.pyplot as plt
import random

lista_cara = []
cara = 0
lista_coroa = []
jogada = []
coroa = 0
jogadas = 50

for i in range(1, jogadas + 1):  
    escolha = random.randint(1, 2)  
    if escolha == 1:
        lista_coroa.append(coroa / i)
        cara += 1
        lista_cara.append(cara/i)
        jogada.append(i)
    else:
        lista_cara.append(cara/i)
        coroa += 1
        lista_coroa.append(coroa / i)
        jogada.append(i)

#lista_cara <-- lista para cara 
#lista_coroa <-- lista para coroa
#jogada <-- lista de jogadas
plt.plot(jogada, lista_cara, label="Cara", color="red")
plt.plot(jogada, lista_coroa, label="Coroa", color="blue") 
# Definir as marcações no eixo y
plt.yticks([i / 10 for i in range(11)])

# Título, legenda e grid
plt.legend()
plt.title('Probabilidade de Cara e Coroa')
plt.grid(True)
