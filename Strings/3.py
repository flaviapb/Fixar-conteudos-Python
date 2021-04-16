# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

nome = str(input("Digite seu nome: "))

for i in range(len(nome)):
    print(nome[i])