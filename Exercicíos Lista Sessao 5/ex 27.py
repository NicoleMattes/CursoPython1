"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias.
    - Infantil A -> 5 a 7 anos
    - Infantil B -> 8 a 10 anos
    - Juvenil A -> 11 a 13 anos
    - Juvenil B -> 14 a 17 anos
    - Senior -> Maiores de 18 anos
"""

# Entrada de dados

idd = int(input('Informe a idade do nadador \n'))
while idd < 5:
    print('Idade não permitida. \n'
          'Somente acima de 5 anos\n')
    idd = int(input('Digite a idade do nadador\n'))

if 4 >= idd <= 7:
    print('Infantil A\n')

elif 8 >= idd <= 10:
    print('Infantil B\n')

elif 11 >= idd <= 13:
    print('Juvenil A\n')

elif 14 >= idd <= 17:
    print('Juvenil B\n')

elif idd >= 18:
    print('Sênior\n')
