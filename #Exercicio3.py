#Exercicio3
'''Elaborar uma função (com retorno) que retorna o cálculo do volume de uma esfera.Sendo que
o raio é passado por parâmetro.'''

from math import pi

def V(raio):

    volume_esfera = (4/3) * pi * (raio ** 3)
    print('O volume do raio {} é {:.2f}'.format(raio, volume_esfera))
    return raio


raio = float(input('Digite o raio da esfera:'))
resultado = V(raio)
print(resultado)
