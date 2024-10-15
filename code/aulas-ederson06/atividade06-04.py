n1=float(input("Informe a noda do 1° bimestre : "))
n2=float(input("Informe a noda do 2° bimestre : "))
n3=float(input("Informe a noda do 3° bimestre : "))
n4=float(input("Informe a noda do 4° bimestre : "))
nota= (n1+n2+n3+n4)/4
if nota>=9.1 and nota<=10:
    conceito="A"
    ap="APROVADO"
elif nota<=9.0 and nota>=7.6:
    conceito="B"
    ap="APROVADO"
elif nota >= 6.0 and nota <=7.5:
    conceito="C"
    ap="APROVADO"
elif nota >= 4.1 and nota <=5.9:
    conceito="D"
    ap="REPROVADO"
elif nota >= 4.0 and nota <=0:
    conceito="E"
    ap="REPROVADO"
print("A notas é %.2f %.2f %.2f %.2f \nA media é: %.2f\nConceito %s\nVoçe esta %s"%(n1,n2,n4,n4,nota,conceito,ap))