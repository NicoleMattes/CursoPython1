"""
Faça um programa que calcule a área de um triângulo, cusa base e altura são fornecidos pelo usuário. Esse programa
não pode permitir a entrada de dados invalidos, ou seja, medidas menor ou igual a 0
"""

# area do triangulo = (base*altura)/2

#entrada de dados

print('Os valores devem ser positivos e maiores que 0\n')

b = float(input('Digite o tamanho da base\n'))
h = float(input('Digite o valor da altura\n'))
area = float()

# verificação se os valores são validos

while b <=0:
    print('Valor da altura é INVALIDO\n')
    b = float(input('Digite o valor da base\n'))
    if h <0:
        print('Valor da altura é INVALIDO\n')
        h = float(input('Digite o valor da altura\n'))

# processamento - calculo da area:

area = (b*h)/2

# saida

print(f'A area é {area}')
