"Desenvolvido por Flávia Renata"

"Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que são ímpares, e que se encontram no intervalo de 1 até 500."

soma = 0
for i in range (1,500+1):
    if i % 3 == 0 and i % 2 == 1:
        soma += i
print(soma)
