#Exercicio7
'''Elaborar uma Função (sem retorno) que ao receber um número deve converter para 
Kelvin e exibe o resultado na tela. A Formula de conversão é
K = cels+273,15'''

cels = float(input('Digite o valor para converter para Fahreinheit:'))

def K(graus):
    valor_kelvin = cels + 273.15
    print('{} Celsius convertidos para Kelvin é {}'.format(graus, valor_kelvin))

resultado = K(cels)
print(resultado)
