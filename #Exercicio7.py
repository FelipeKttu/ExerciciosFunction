#Exercicio7
"""Elaborar uma função (com retorno) que determina se um número passado como parâmetro é primo.
A função quando chamada retorna 1 indicando que o número é primo e 0 caso contrário"""

def pri(num):
  CD = 0
  C = 0
  while C < N:
    C += 1
    if N % C == 0:
      print('{} é divisivel por {}'.format(N,C))
      CD += 1
    else:
      print('{} não é divisel por {}'.format(N,C))

  if CD <= 2:
    print('{} é primo !'.format(N))
    return 1
  elif CD > 2:
    print('{} não é primo !'.format(N))
    return 0
  

N = float(input('Digite o número para verificar se é primo:'))
print(pri(N))

         
       