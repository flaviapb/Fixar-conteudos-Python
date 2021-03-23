"Desenvolvido por Flávia Renata"

"Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."

ano_nascimento = int(input("Digite o ano do seu nascimento: "))

cont = 18 #idade para poder se alistar 

if ano_nascimento > 2003:
    idade = 2021 - ano_nascimento
    qntd_anos = cont - idade
    print("No ano de 2021, você tem {} anos, logo: Você vai se alistar daqui há {} anos/ano!".format(idade, qntd_anos))

elif ano_nascimento < 2003:
    idade = 2021 - ano_nascimento
    qntd_anos = idade - cont 
    print("No ano de 2021, você tem {} anos, logo: Você devia ter se alistado há {} anos/ano !".format(idade, qntd_anos))

elif ano_nascimento == 2003:
    idade = 2021 - ano_nascimento
    qntd_anos = idade - cont 
    print("No ano de 2021, você tem {} anos, logo: Você se alista nesse ano !".format(idade))