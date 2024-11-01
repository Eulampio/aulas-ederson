#A série de fibonate é formada pela seguência  0,1,1,2,3,5,8,13,21,34,55,,,,,Faça  um programa capaz de gerar a serie o n n-ésimo termo
a=5
n=1
n2=1
n3=0
print(0,end=" ")
for i in range (0,a):
    if( i ==0 or i==1):
        print(1, end=" ")
    else:
        n3= n + n2
        n = n2
        n2= n3
        print(n3,end=" ")
    

   
