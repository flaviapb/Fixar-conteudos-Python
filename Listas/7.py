# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
soma = 0
multi = 1

for i in range(5):
    num = int(input("Digite seu {}º número: ".format(i+1)))
    lista.append(num)

for i in range(len(lista)):     
    soma += lista[i]
    multi *= lista[i]

print("A soma dos números da lista é: {}".format(soma))
print("A multiplicação dos números da lista é: {}".format(multi))
print("A lista completa: {}".format(lista))
