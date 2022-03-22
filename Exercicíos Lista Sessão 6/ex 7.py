"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""

cont = 0
num = 0
media = 0

print('Digite 10 valores')
while cont < 10:
    num = int(input())
    if num > 0:
        media = media + num
        cont = cont + 1
    print(f'cont: {cont}')
print(f'{media/10}')
