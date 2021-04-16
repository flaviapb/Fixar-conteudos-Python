#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
soma = 0
for i in range(4):
    nota = float(input("Digite sua {}º nota: ".format(i+1)))
    notas.append(nota)
    soma += nota 

print("Sua média é: {:.1f}".format(soma/len(notas))) #Ou soma/4, poderia colocar o 4 já que a questão fala que vão ser 4 notas