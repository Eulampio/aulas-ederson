# %d - inteiro 
# %s - string
# %f - float (numeros de com casas decimais)
# %b - bool (verdadeiro ou falso) 
salario=float(input("Informe seu salario: "))
if salario<=280:
    percentual=20


elif salario>280 and salario<700:
    percentual=15
elif salario>=700 and salario<1500:
    percentual=10
elif salario>=1500:
    percentual=5






aumento = (percentual/100)*salario
total=salario+aumento


print("Salario era de: %.2f \nO percentual de almento: %.2f porcento\nO valor do aumento foi de :%.2f \nO total foi de %.2f "%(salario,percentual,aumento, total) )