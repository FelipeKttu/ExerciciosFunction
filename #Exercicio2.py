#Exercicio2
'''Elaborar uma função (com retorno) que verifica se um número é positivo ou negativo.sendo
que o valor de retorno será 1 se positivo, -1 se for negativo e 0 se for igual a 0'''

N1 = float(input('Digite um número:'))

def V(N):
  if N1 > 0:
    print('{} é positivo !!'.format(N1))
    return 1
  elif N1 < 0:
    print('{} é negativo !!'.format(N1))
    return -1
  elif N1 == 0:
    print('{} é neutro !!'.format(N1))
    return 0

resultado = V(N1)
print(resultado)