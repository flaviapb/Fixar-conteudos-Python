"Desenvolvido por Flávia"

"Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."


valor_casa =  float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite seu salario, comprador: "))
qntd_anos = int(input("Em quantos anos você vai pagar, comprador: "))

prestacao = valor_casa / (qntd_anos * 12)
min_salario = salario_comprador * (30/100)

if prestacao > min_salario:
    print("Seu emprestimo foi NEGADO!")

else:
    print("Seu emprestimo foi APROVADO!") 

#caso deseja saber o motivo de ser aprovado\reprovado:

#print("Valor esperado {:.2f} - O que seu salario consegue de acordo com nossas regras {:.2f}".format(prestacao,min_salario))