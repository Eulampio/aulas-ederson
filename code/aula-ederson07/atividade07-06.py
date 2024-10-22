
a =float(input("insira a população da cidade A: "))
t1 =float(input("informe a taxa de crescimento cidade B: "))
b =float(input("informe a população da cidade B: "))
t2=float(input("informe a taxa de cescimento cidade B: "))
tax1= t1/100
tax2= t2/100
cont=0 
while True:
    a+=a*tax1
    b+=b*tax2
    cont=cont+1
    if a>=b:
        break
print (cont)    



