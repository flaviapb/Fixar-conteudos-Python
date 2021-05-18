print("""Suas opções: + --> Para realizar soma
             - --> Para realizar Subtração
             / --> Para realizar divisão
             x --> Para realizar multiplicação \n""")
while True:
    sinal = input("Digite o simbolo para sua operação: ").lower()
    if sinal == "+" or sinal == "-" or sinal == "/" or sinal == "x":
        break
    else:
        continue

num = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))


def calculadora(num,num2,sinal):
    if sinal == "+":
        return num+num2
    elif sinal == "-":
        return num-num2
    elif sinal == "/":
        try:
            return num/num2
        except:
            return "Impossivel divisão por zero"
    elif sinal == "x":
        return num * num2

print("O resultado é: {}".format(calculadora(int(num),int(num2),sinal)))

while True:
    continuar = input("Você deseja continuar: ").lower()
    if continuar == "sim":
        num1 = float(input("Digite o 1º número: "))
        num3 = float(input("Digite o 2º número: "))
        sinal = input("Digite o simbolo para sua operação: ").lower()
        calculadora(num1,num3,sinal)
        print("O resultado é: {}",format(calculadora(int(num1),int(num3),sinal)))
    else:
        print("Até mais usuário")
        break