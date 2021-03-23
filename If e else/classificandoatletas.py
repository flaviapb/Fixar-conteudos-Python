"Desenvolvido por Flávia Renata"

'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER '''

ano_nascimento = int(input("Digite o ano do seu nascimento: "))

#ano = 2021 -- ano que usei para resolver o problema 

idade = 2021 - ano_nascimento


if idade <= 9:
    print("Você é um 'Atleta Mirim', pois você têm: {} anos".format(idade))

if idade > 9 and idade <= 14:
    print("Você é um 'Atleta Infantil', pois você têm: {} anos".format(idade))

if idade > 14 and idade <= 19:
    print("Você é um Atleta Júnior, pois você têm: {} anos".format(idade))

if idade > 19 and idade <= 25:
    print("Você é um Atleta Sênior, pois você têm: {} anos".format(idade))

if idade > 25:
    print("Você é um Atleta Master, pois você têm: {} anos".format(idade))