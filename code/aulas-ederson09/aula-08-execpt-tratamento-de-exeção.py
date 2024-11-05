try:
    a=int(input("Digite um palavra: "))
except ValueError:
    print("Digite apenas um numero")    
except:
    print("erro desconhecido")  

