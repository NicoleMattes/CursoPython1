"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares
"""

print('digite um número')
N = int(input())
for i in range(0, N):
    if i%2 == 1:
        print(f'{i}')
