"""
Leia um número fornecido por um usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número
for negativo, mostre uma mensagem dizendo que o número negativo é invalido
"""

import math

print(' Digite um número')
num = float(input())

if num >= 0:
    rqd = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {rqd}')
else:
    print(f'O número {num} é invalido')

