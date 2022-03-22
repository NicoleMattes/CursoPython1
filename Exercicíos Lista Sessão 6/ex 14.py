"""
Faça um programa que leia um número inteiro positivo impar N e imprita toros os pares de 0 até N em ordem
descrecente
"""

n = int(input('digite um número \n'))

for i in range(0, n):
    if i % 2 == 1:
        print(f'{i}')

