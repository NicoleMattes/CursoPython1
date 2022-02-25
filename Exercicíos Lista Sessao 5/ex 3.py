"""
Leia um número real. Se o número for possitivo imprima a raiz quadrada, do contrario imprima
o número ao quadrado
"""
import math

print(f'Digite um número')
num = float(input())

if num >= 0:
    rqd = math.sqrt(num)
    print(f'A raiz quadrada do número {num} é {rqd}')

else:
    qd = num**num
    print(f"O número {num} ao quadrado é {qd}")
