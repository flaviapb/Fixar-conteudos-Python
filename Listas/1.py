#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range(10):
    num = int(input("Digite o {}ª número da lista: ".format(i+1)))
    lista.append(num)


#lista.sort(reverse=True) #pode ser assim
lista.reverse() #ou assim 

print(lista)