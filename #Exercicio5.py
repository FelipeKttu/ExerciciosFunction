#Exercicio4
'''Elaborar uma função (sem retorno) que ao receber um número deve converter para 
fahrenheit e exibe o resultado na tela. A formula de conversão é
F = (9 * C + 160) / 5'''
C = float(input('Digite o valor para converter para Fahreinheit:'))

def F(graus):
    VF = (C * 1.8)+ 32
    print('{} Celsius convertidos para Fahrenheit é {}'.format(C,VF))
    return C

resultado = F(C)
print(resultado)

