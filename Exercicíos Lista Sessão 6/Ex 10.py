"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
"""

soma = int()
for n in range(0, 100):
    if n%2 == 0:
        soma = soma + n
print(f'{soma}')

