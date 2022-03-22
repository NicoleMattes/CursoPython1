"""
Faça um program que peça para o usuário digitar 10 valores e some-os
"""

num = 0
soma = 0

for i in range(0, 10):
    num = float(input())
    soma = soma + num
print(f'{soma}')