"Desenvolvido por Flávia Renata"

" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto. "

sexo = str(input("Sexo: ")).upper()

while sexo not in 'FfMnm':
    sexo = str(input("Sexo invalido, digite novamente: ")).upper()
    
print("O sexo {} consta no sistema!".format(sexo))
