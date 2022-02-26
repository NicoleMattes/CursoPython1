"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se o número for possitivo,
Calcular o logaritimo desse número
"""

import math

print('Digite um número')
num = float(input())

if num < 0:
    print("Numero invalido")
else:
    print(f"{math.log(num)}")
