#Exercicio6
'''Elaborar uma Função (sem retorno) que ao receber um número deve converter para 
Kelvin e exibe o resultado na tela. A Formula de conversão é
K = C+273,15'''

C = float(input('Digite o valor para converter para Fahreinheit:'))

def K(graus):
    VK = C + 273.15
    print('{} Celsius convertidos para Kelvin é {}'.format(C,VK))
    return VK

resultado = K(C)
print(resultado)
