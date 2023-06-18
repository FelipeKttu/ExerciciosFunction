#Exercicio1 
'''Elaborar uma função (com retorno) que recebe como parâmetro um número inteiro
e devolve o seu dobrar.'''

N = float(input('Digite o número:'))

def dobrar(num):
    print('O número é {}'.format(num))

    dobro = N * 2

    print('O dobro é {}'.format(num))
    return N

resultado = dobrar(N)
print(resultado)
