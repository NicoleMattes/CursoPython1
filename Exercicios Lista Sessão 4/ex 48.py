"""
Faça um programa que leia um valor inteiro em segundos e imprima-o em horas, minutos e segundo.
"""

print('Digite um valor em segundos')
seg = int(input())

min = seg/60
print(f'O tempo em minutos é {min}')
horas = min/60
print(f'O temppo em horas é de {horas}')