"Desenvolvido por Flávia Renata"

"Escreva um programa que leia dois, ou mais, números inteiros e compare-os. mostrando na tela"

vezes = int(input("Quantos números vc quer comparar? "))
cont = 0
lista = []
while cont < vezes:
    num = int(input("Digite o número: "))
    lista.append(num)
    cont += 1

print("Comparando os {} valores digitados, o maior número é {}!".format(vezes, max(lista)))