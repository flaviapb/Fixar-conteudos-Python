#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

meses = ["Janeiro","Fevereiro","Março","Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp_total = []
soma = 0
media = 0
maior = []

for i in range(len(meses)):
    temp_mes = float(input("Digite a temperatura de {}: ".format(meses[i])))
    temp_total.append(temp_mes)
    soma += temp_mes
    media = soma/len(meses)

for i in range(len(temp_total)):
    if temp_total[i] > media:
        print (str(i+1) + " - " + meses[i])