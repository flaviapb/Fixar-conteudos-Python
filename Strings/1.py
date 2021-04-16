''' Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.'''


string1 = str(input("Digite a primeira string: "))
string2 = str(input("Digite a segunda string: "))

print("String 1: {}".format(string1))
print("String 2: {}".format(string2))
print("Tamanho de {}: {}".format(string1,len(string1)))
print("Tamanho de {}: {}".format(string2,len(string2)))


if len(string1) == len(string2):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")

if string1 == string2:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")