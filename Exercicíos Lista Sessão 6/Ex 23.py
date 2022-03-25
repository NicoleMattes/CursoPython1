"""
Faça um algoritmo que leia um número possitivo e imprima seus divisores
"""

n = int(input('Digite um número\n'))

for i in range(1, n):
    if n%i == 0:
        print(f'n é divisivel por {i}')
