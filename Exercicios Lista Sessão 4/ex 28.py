# Faça a leitura de 3 valores e apresente como resultado a soma dos quadrados dos três valroes lidos

import math


print('Digite três valores, espaçados pelo enter')
v1 = float(input())
v2 = float(input())
v3 = float(input())
print(f'Os valoers lidos foram {v1}, {v2} e {v3}')

raiz = math.sqrt(v1)
raiz2 = math.sqrt(v2)
raiz3 = math.sqrt(v3)

print(f'o Valor da raiz quadrada dos respectivos números são {raiz}, {raiz2} e {raiz3}')

s = raiz+raiz2+raiz3

print(f'A soma das raizers quadradas é de {s}')
