"""
Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais
"""

n = int(input('Digite um número inteiro \n'))
soma = float()

for i in range(0, n):
    soma = soma + i
    print(f'{soma}')

