while True:

    a=int(input("informe a nota: "))
    if a>-1 and a<11 :
        print("nota é %d"%(a))
        break
    else:
        print("nota não valida")
        