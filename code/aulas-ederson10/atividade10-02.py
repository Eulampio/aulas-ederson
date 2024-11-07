def p(x):

    if x==0:
        return 
    elif x>0:
        return True

    else :
        return False

    
    
    
while True:
    nun=int(input("inira um numero: "))
    if p(nun) == True:
        print("É positivo:" ,nun)
    elif p(nun) == False:
        print("O Negativo : ",nun)
    else:
        print("VALOR 0 ")