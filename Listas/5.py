# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista_par = []
lista_impar = []
lista_geral = []

for i in range(20):
    num = int(input("Digite seu {}ª número: ".format(i+1)))
    lista_geral.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print("Lista geral: {}".format(lista_geral))
print("Lista com números pares: {}".format(lista_par))
print("Lista com números impares: {}".format(lista_impar))