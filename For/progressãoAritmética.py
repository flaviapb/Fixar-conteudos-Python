"Desenvolvido por Flávia Renata"

"Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
decimo_termo = termo + (10-1) * razao
for i in range(termo, decimo_termo+1, razao):
    print(i, end=" ")1