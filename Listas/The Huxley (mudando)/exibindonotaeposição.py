
'''Testando formas diferentes, questão The Huxley 

# --> Diferença só no print da media:
# --> Pode ser feito: 
     --> print("Media: {:.2f}".format(soma/len(notas)))
                    #ou
     --> print("Media: {:.2f}".format(soma/qntd)) '''

notas = []
soma = 0
while True:
    qntd = int(input())
    if qntd <= 0 or qntd > 5:
        print("Numero de notas invalido.")
        break
    else:
        for i in range(qntd):
            nota = float(input())
            notas.append(i)
            soma += nota
            print("Nota {}: {}".format(notas[i] +1,nota))
    print("Media: {:.2f}".format(soma/qntd))
    break


    