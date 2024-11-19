def par(x):
    if (x%2)==0:
        return True
    else:
        return False
while True:
    nun=int(input("isira um numero: "))
    if par(nun):
        print("É par:" ,nun)
    else:
        print("É impar: ",nun)
