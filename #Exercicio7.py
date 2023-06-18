#Exercicio7
"""Elaborar uma função (com retorno) que determina se um número passado como parâmetro é primo.
A função quando chamada retorna 1 indicando que o número é primo e 0 caso contrário"""

def primo(num):
  vezes_divido = 0
  cont = 0

  while cont < num:

    cont += 1
    if num % cont == 0:
      print('{} é divisivel por {}'.format(num, cont))
      vezes_divido += 1
    else:
      print('{} não é divisel por {}'.format(num, cont))

  if vezes_divido <= 2:
    print('{} é primo !'.format(num))
    return 1
  
  elif vezes_divido > 2:
    print('{} não é primo !'.format(num))
    return 0
  

numero = float(input('Digite o número para verificar se é primo:'))
print(primo(numero))
