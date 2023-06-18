#Exercicio4
'''Elaborar uma função (sem retorno) que ao receber um número deve converter para 
fahrenheit e exibe o resultado na tela. A formula de conversão é
F = (9 * celsius + 160) / 5'''

cels = float(input('Digite o valor para converter para Fahreinheit:'))

def F(graus):
    VF = (graus * 1.8)+ 32
    print('{} Celsius convertidos para Fahrenheit é {}'.format(graus, VF))
    return cels

resultado = F(cels)
print(resultado)


