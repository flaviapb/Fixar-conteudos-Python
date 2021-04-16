# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []

for i in range(10):
    letras = str(input("Digite a {}ª letra: ".format(i+1)))
    if letras != "a" and letras != "e" and letras != "i" and letras != "o" and letras != "u":
        lista.append(letras)
print(lista)