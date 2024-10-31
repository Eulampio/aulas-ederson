
a=int(input("dgt um valor "))
b=int(input("dgt um valor "))
c=int(input("dgt um valor "))



if a>=1 or b>=1 or c>=1:
        print("invalida")
elif a<=0 or b<=0 or c<=0:
        print("invalida")

elif a==0 and b==0 and c==1:
        print("verde on")
        print(a,b,c)
elif a==1 and b==0 and c==0:
        print("vermelho on")
        print(a,b,c)
elif a==0 and b==1 and c==0:
        print("amarelo on")
        print(a,b,c)
elif a==1 and b==0 and c==1:
        print("invalida")
        print(a,b,c)
elif a==0 and b==0 and c==0:
        print("desligado ")
        print(a,b,c)
    









