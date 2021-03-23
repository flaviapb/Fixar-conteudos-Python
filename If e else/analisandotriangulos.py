"Desenvolvido por Flávia Renata"

''' Calcule qual o tipo de um triângulo, sabendo que:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes '''

seg1= float(input("Digite o primeiro segmento: "))
seg2 = float(input("Digite o segundo segmento: "))
seg3 = float(input("Digite o terceiro segmento: "))


if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg1 + seg2):
    
    if seg1 == seg2 == seg3:
        print("Seus segmentos formaram um triângulo equilátero")
    
    elif (seg1 != seg2 != seg3 != seg1):
        print("Seus segmentos formaram um triângulo escaleno")
    
    else:
        print("Seus segmentos formaram um triângulo isósceles")

else:
    print("Esses segmnentos não formam um Triângulo")