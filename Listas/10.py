# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista1 = []
lista2= []
lista3 = []

for i in range(4):
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

print("Sua terceira lista, com os elementos das listas 1 e 2: {}".format(lista3))