# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

lista_idade = []
lista_altura = []
qntd_alunos = 0
soma = 0
media = 0

for i in range(30):
    idade = int(input("Digite sua idade, {}ª aluno: ".format(i+1)))
    if idade > 13:
        lista_idade.append(idade)
    altura = float(input("Digite sua altura, {}ª aluno: ".format(i+1)))
    lista_altura.append(altura)
    soma += altura
    media = soma/30

for i in range(30):
    if lista_idade[i] > 13 and lista_altura[i] < media:
        qntd_alunos += 1

print("A quantidade de alunos com altura menor que da turma de 30 alunos são: {}".format(qntd_alunos))