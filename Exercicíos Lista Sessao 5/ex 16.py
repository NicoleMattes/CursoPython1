"""
Usando um Switch, faça um proframa que receba um número de 1 a 12 e imprima o mês correspondendo ao número. Isso é
Janiero é 1, Fevereiro 2 e assim por diante.
"""

meses = ['Janeiro',
         'Fevereiro',
         'Março',
         'Abril',
         'Junho',
         'Julho',
         'Agosto',
         'Setembro',
         'Outubro',
         'Novembro',
         'Dezembro']

mes = int(input('Digite um número\n'))

if 1 < mes > 12:
    print('O número digitado é invalido')

else:
    print(f'O dia selecionado é: {meses[mes - 1]}.')
