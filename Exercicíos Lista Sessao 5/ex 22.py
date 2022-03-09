"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para
aposentadoria são:
    - Ter pelo menos 65 anos;
    - Ou ter trabalhado 35 anos;
    - Ou ter pelo menos 60 anos e 25 anos trabalhados.
"""

idade = int(input('Qual a idade?\n'))
anos_trabalhados = int(input('Quantos anos trabalhando\n'))

if idade >= 65:
    print('Aposentadoria ACEITA')

elif idade >= 60 and anos_trabalhados >= 25:
    print('Aposentadoria ACEITA')

elif anos_trabalhados >= 35:
    print('Aposentadoria ACEITA')

else:
    print('Aposentadoria NEGADA')
