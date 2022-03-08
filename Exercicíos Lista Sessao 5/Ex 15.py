"""
Usando Switch, escreva um programa que leia un inteiro entre 1 e 7 e imprima o dia da semana correspondente
Isso é, domingo é 1, segunda 2 e asim por diante.
"""

diasemana = ['domingo',
             'segunda',
             'terça',
             'quarta',
             'quinta',
             'sexta',
             'sábado']

dia = int(input('Digite um número de 1 a 7\n'))

if 1 < dia > 7:
    print('Esse dia não existe')
else:
    print(f'O dia da semana selecionado é: {diasemana[dia - 1]}.')