#Exercicio2
'''Elaborar uma função (com retorno) que verifica se um número é positivo ou negativo.sendo
que o valor de retorno será 1 se positivo, -1 se for negativo e 0 se for igual a 0'''

num1 = float(input('Digite um número:'))

def FunVer(N):
  if num1 > 0:
    print('{} é positivo !!'.format(num1))
    return 1
  
  elif num1 < 0:
    print('{} é negativo !!'.format(num1))
    return -1
  
  elif num1 == 0:
    print('{} é neutro !!'.format(num1))
    return 0

resultado = FunVer(num1)
print(resultado)
