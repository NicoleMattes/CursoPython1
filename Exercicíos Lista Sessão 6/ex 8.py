"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""

num = 0
menor = float()
maior = float()

print('Digite 10 valores')
for i in range(0, 10):
    num = float(input())
    if i == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'maior: {maior}')
print(f'menor: {menor}')