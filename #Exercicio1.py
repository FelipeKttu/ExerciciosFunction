#Exercicio1 
'''Elaborar uma função (com retorno) que recebe como parâmetro um número inteiro
e devolve o seu dobro.'''

N1 = float(input('Digite o número:'))

def dobro(N):
    print('O número é {}'.format(N))
    D = N1 * 2
    print('O dobro é {}'.format(D))
    return N1

resultado = dobro(N1)
print(resultado)