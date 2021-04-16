# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista1 = []
lista2= []
lista3 = []

for i in range(10):
    num1 = int(input("Digite o {} número para o 1º vetor: ".format(i+1)))
    print("\n")  #Aqui poderia ser feito outro for tambêm, para prencher a segunda lista separadamente.
    num2 = int(input("Digite o {} número para o 2º vetor: ".format(i+1)))
    print("\n")
    lista1.append(num1)
    lista2.append(num2)

print("Sua primeira lista: {}".format(lista1))
print("Sua segunda lista: {}".format(lista2))


for i in range(len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    if len(lista3) == len(lista2):
        break
    else:
        continue

print("Sua terceira lista, com os elementos das listas 1 e 2: {}".format(lista3))



''' for x in range(10):
    num2 = int(input("Digite o {} número para o 2º vetor: ".format(x+1)))
    lista2.append(num)
for l in range(10):
    num3 = int(input("Digite o {} número para o 3º vetor: ".format(l+1)))
    lista3.append(num) '''