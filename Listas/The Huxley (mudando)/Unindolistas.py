lista1 = []
lista2 = []
while True:
    tamanho1 = int(input())
    if tamanho1 == 0:
        print("Erro - A lista deve ter pelo menos 1 elemento.")
        break
    else:
        for i in range (tamanho1):
            num1 = int(input())
            lista1.append(num1)

        tamanho2 = int(input())
        if tamanho2 == 0:
            print("Erro - A lista deve ter pelo menos 1 elemento.")
            break
        else:
            for i in range (tamanho2):
                num2 = int(input())
                lista2.append(num2)

    print( *(lista1 + lista2), end=" ") #end ou sep, tanto faz
    break

    
