#Exercicio4
'''Elaborar uma função (sem retorno) que recebe dois valores inteiros passados como parâmetro 
logo em seguida a função deve exibir um menu com 4 opções:'''
from math import sqrt

def Menu(valor_1,valor_2):
    print('-'*5,'Menu','-'*5)
    print("""Para Soma digite 1\nPara Subtrair digite 2\nPara Multiplicar digite 3\nPara dividir digite 4\npara raiz quadrada do prímeiro número digite 5""")
    
    E = int(input('Digite:'))

    soma = valor_1 + valor_2
    subtracao = valor_1 - valor_2
    multiplicacao = valor_1 * valor_2
    divisao = valor_1 / valor_2
    raiz = sqrt(valor_1)

    if E == 1:
        print('A soma de {} com {} é {}'.format(valor_1, valor_2, soma))
    elif E == 2:
        print('A subtração de {} por {} é {}'.format(valor_1, valor_2, subtracao))
    elif E == 3:
        print('A multiplicação de {} com {} é {}'.format(valor_1, valor_2, multiplicacao))
    elif E == 4:
        print('A divisão de {} com {} é {}'.format(valor_1, valor_2, divisao))
    elif E == 5:
        print('A raiz quadrada de {} é {}'.format(valor_1, raiz))


valor_1 = float(input('Digite o primeiro número:'))
valor_2 = float(input('Digite o segundo número:'))
print(Menu(valor_1, valor_2))
