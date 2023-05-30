#Exercicio4
'''Elaborar uma função (sem retorno) que recebe dois valores inteiros passados como parâmetro 
logo em seguida a função deve exibir um menu com 4 opções:'''
from math import sqrt

def Menu(V1,V2):
    print('-'*5,'Menu','-'*5)
    print("""Para Soma digite 1\nPara Subtrair digite 2\nPara Multiplicar digite 3\nPara dividir digite 4\npara raiz quadrada do prímeiro número digite 5""")
    E = int(input('Digite:'))
    S = V1 + V2
    SU = V1 - V2
    M = V1 * V2
    D = V1 / V2
    R = sqrt(V1)
    if E == 1:
        print('A soma de {} com {} é {}'.format(V1,V2,S))
    elif E == 2:
        print('A subtração de {} por {} é {}'.format(V1,V2,SU))
    elif E == 3:
        print('A multiplicação de {} com {} é {}'.format(V1,V2,M))
    elif E == 4:
        print('A divisão de {} com {} é {}'.format(V1,V2,D))
    elif E == 5:
        print('A raiz quadrada de {} é {}'.format(V1,R))


V1 = float(input('Digite o primeiro número:'))
V2 = float(input('Digite o segundo número:'))
print(Menu(V1,V2))

