n=int(input("n de doces: "))
x=int(input("doces para primeira evolucao: "))
y=int(input("doces para segunda evolucao: "))
z=int(input("doces para terciera evolucao: "))

if n<=0 and n<1001:
        print("não pode evoluir")
elif x<=1 and x<1001:
        print("não pode evoluir2")
elif y<=1 and y<1001:
        print("não pode evoluir3")
elif z<=1 and z<1001:
        print("não pode evoluir4")


if x+y+z<=n:
        print(3)
elif x+y<=n or y+z<n or x+z<=n:
        print(2)
elif n>=x or n>=y or n>=z:
        print(1)

        
        














