#faça um programa em linguagem python que o nome idade, sexo, e receba duas 
# notas e calcule a media aritimetica e mostre o resultaFZ
nome=str(input("Informe o nome: "))
idade=int(input("Informe a idade: "))
sexo=str(input("Informe o sexo: "))
nota1=float(input("Informe a primeita nota: "))
nota2=float(input("Informe a segunda nota"))
media=float(nota1+nota2)/2
print("o nome do(a) é %s a idade é %d o sexo é %s a media de %.2f "%(nome,idade,sexo,media))