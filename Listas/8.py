#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

lista_idade = []
lista_altura = []

for i in range(5):
    idade =  int(input("Digite sua idade, cliente {}: ".format(i+1)))
    lista_idade.append(idade)
    altura = float(input("Digite sua altura, cliente {}: ".format(i+1)))
    lista_altura.append(altura)

lista_idade.reverse()
lista_altura.reverse()

print("Lista das idades: {}".format(lista_idade))
print("Lista das alturas: {}".format(lista_altura))