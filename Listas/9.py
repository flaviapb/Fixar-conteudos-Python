# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

lista = []
quadrado = 1
soma = 0
for i in range(10):
    num = int(input("Digite seu {}º número: ".format(i + 1)))
    lista.append(num)

    quadrado = lista[i] * lista[i]
    soma += quadrado
    
print("A soma dos quadrados é igual: {}".format(soma))
print("Os números utilizados para fazer a soma dos quadrados foram: {}".format(lista))