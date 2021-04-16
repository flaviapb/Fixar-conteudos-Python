''' Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
        "Telefonou para a vítima?"
        "Esteve no local do crime?"
        "Mora perto da vítima?"
        "Devia para a vítima?"
        "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''


sim = 0
nao = 0

lista = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

for i in range(len(lista)):
    pergunta = str(input("{}: ".format(lista[i]))).upper()

    if pergunta == "SIM":
        sim += 1
    else:
        nao += 1

if sim == 2:
    print("Suspeita")
elif sim > 2 and sim <= 4:
    print("Cúmplice")
elif sim > 4:
    print("Assasino")
else:
    print("Inocente")