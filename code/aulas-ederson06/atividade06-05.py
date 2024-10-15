p1=str(input("Telefonou para a Vítima? "))
p2=str(input("Esteve no local do crime? "))
p3=str(input("Morava perto da vítima? "))
p4=str(input("Devia para a Vítima? "))
p5=str(input("Já trabalhou com a Vítima? "))
cont=0
if p1=="sim":
    cont= cont+1
if p2=="sim":
    cont= cont+1
if p3=="sim":
    cont= cont+1
if p4=="sim":
    cont= cont+1
if p5=="sim":
    cont= cont+1
if cont==2:
    print("Suspeito")
elif cont==3 or cont==4:
    print("Cumplice")
elif cont==5:
    print("Assassino")
elif cont==1 or cont==0:
    print("Inocente")