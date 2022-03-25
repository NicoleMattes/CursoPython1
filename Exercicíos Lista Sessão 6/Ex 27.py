"""
Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica:
    h(n) = (1 +1) + (2 + 1) + (3 +1) + (4 + 1) .... (n + 1)
Faça um programa que leia o valor n e apresente o valor de H
"""

n = int(input('Digite um valor\n'))
h = int()
hh = int()

for i in range(1, n+1):
    hh = i + 1
    print(f'{hh}')
    h = hh + hh
print(f'H: {h}')

