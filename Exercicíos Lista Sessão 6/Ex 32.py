"""
Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saida o número de cada dado
e a relação entre eles (>,<,=) de cada lançamento.
"""

import random

d1 = int()
d2 = int()

vz = int(input('Digite quantas vezes os dados devem ser lançados\n'))

for i in range(1, vz +1):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 > d2:
        print(f'{d1} > {d2}')
    if d1 < d2:
        print(f'{d1} < {d2}')
    if d1 == d2:
        print(f'{d1} = {d2}')
