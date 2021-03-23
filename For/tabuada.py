"Desenvolvido por Flávia Renata"

"Mostre a tabuada de um número que o usuário escolher"

num = int(input("Digite um nùmero para sua tabuada: "))

for i in range(1,11):
    print("{} x {} = {}".format(num,i,num*i))