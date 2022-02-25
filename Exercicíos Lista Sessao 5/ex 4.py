"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada do número digitado
"""

import math

print('Digite um numero')
num = float(input())

if num >= 0:
    nq = num**num
    rqd =math.sqrt(num)
    print(f'O número {num} ao quadrado é {nq} e a raiz quadrado é {rqd}')

else:
    print('O número é invalido')