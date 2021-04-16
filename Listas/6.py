# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

lista = []
for i in range(10):
    nota1 = float(input("Primeira nota do {}ª aluno: ".format(i +1)))
    nota2 = float(input("Segunda nota do {}ª aluno: ".format(i+1)))
    nota3 = float(input("Terceira nota do {}ª aluno: ".format(i+1)))
    nota4 = float(input("Quarta nota do {}ª aluno: ".format(i+1)))
    print("\n")
    media = (nota1 + nota2 + nota3 + nota4)/4
    if media >= 7.0:
        lista.append(media)


print("O total de alunos aprovados foram: {}".format(len(lista)))
    