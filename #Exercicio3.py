#Exercicio3
'''Elaborar uma função (com retorno) que retorna o cálculo do volume de uma esfera.Sendo que
o raio é passado por parâmetro.'''

from math import pi

def V(Raio):
    VE = (4/3) * pi * (R ** 3)
    print('O volume do raio {} é {:.2f}'.format(R,VE))
    return Raio


R = float(input('Digite o Raio da esfera:'))
resultado = V(R)
print(resultado)