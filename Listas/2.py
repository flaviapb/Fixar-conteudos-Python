# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os

lista = []

for i in range(5):
    num = int(input("Digite o {}º numero da lista: ".format(i+1)))
    lista.append(num)

print(lista)