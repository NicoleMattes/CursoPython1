"""
Faça um programa que determine e mostre os 5 primeiros multiplos de três, considerando apenas números maiores que 0
"""

cont = 0
for n in range(0, 50):
    if n % 3 == 0 and n != 0:
        print(f'{n}')
        cont = cont + 1
    if cont >= 5:
        break