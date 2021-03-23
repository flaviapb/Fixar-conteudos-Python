"Desenvolvido por Flávia Renata"

"Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."


num = int(input("Digite um número para a conversão: "))
print("\n")
print("Digite:\n [1] para binário \n [2] para octal \n [3] para hexadecimal")
print("\n")

op = int(input("Sua opção: ")) 

while True:
    if op != 1 or op!= 2 or op!= 3:
        print("ERRO")
        print("\n")
        print("Digite:\n [1] para binário \n [2] para octal \n [3] para hexadecimal")
    op = int(input("Sua opção: "))
    else:
        break

if num == 1:
    print("{} convertido para binario fica {}".format(num, bin(num)))

elif num == 2:
    print("{} convertido para binario fica {}".format(num, oct(num)))

elif num == 3:
    print("{} convertido para binario fica {}".format(num, hex(num)))