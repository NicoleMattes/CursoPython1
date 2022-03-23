"""
Faça um programa que receba dois números. Calcule e mostre
    - A soma dos números pares desse intervalo de números, incluindo os números digitados;
    - A multiplicação dos números ímpares desse intervalo, incluindo os digitados;
"""

print('Digite os dois valores')
n1 = int(input())
n2 = int(input())
soma = int()
mult = 1

for i in range(n1, n2):
    if i % 2 == 0:
        soma = soma + i
    if i % 2 == 1:
        mult = mult * i
print(f'soma: {soma}')
print(f'multiplicação: {mult}')

