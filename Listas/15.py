''' Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem; '''

notas = []
acima = 0
abaixo = 0

while True:
    nota = float(input("Digite sua nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)
        continue

print("\n")
print("A quantidade de notas lidas, foram: {}".format(len(notas)))
print("\n")
print("Sua lista com as notas, da forma que foi digitada: {}".format(notas))
print("\n")
notas.reverse()
for i in range(len(notas)):
    print("Sua lista com as notas, da forma reversa do que foi digitada: {}".format(notas[i]))
print("\n")
print("A soma das suas notas: {}".format(int(sum(notas))))
print("\n")
print("A média de suas notas: {:.1f}".format(sum(notas)/len(notas)))
print("\n")

for i in range(len(notas)):
    if notas[i] > sum(notas)/len(notas):
        acima += 1

print("Valores acima da média : {}".format(acima))
print("\n")

for i in range(len(notas)):
    if notas[i] < 7.0:
        abaixo += 1

print("Valores abaixo de 7.0 : {}".format(abaixo))
print("\n")
print("Fim do programa, obrigada!!")