# leia a altura e o raio de um cilindro e imprima o volume do cilindro

import math

print("Digite a altura do cilindro")
alt = float(input())
print("Digite o raio do cilindro")
raio = float(input())
vol = math.pi * raio ** 2 * alt

print(f"O volume é: {vol}")
