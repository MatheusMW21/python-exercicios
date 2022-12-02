n1 = int(input('Entre aqui com o primeiro número: ')) 
n2 = int(input('Entre aqui com o segundo número: ')) 
n3 = int(input('Entre aqui com o terceiro número: ')) 

if (n1>n2): 
    if(n2>n3):
        print(n3,n2,n1)
    else:
        if (n1>n3):
            print(n2,n3,n1)
        else:
            print(n2, n1, n3)
else: 
    if (n1>n3):
        print(n3,n1,n2)
    else:
        print(n1,n2,n3)