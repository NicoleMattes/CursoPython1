"""
Faça um programa que leia 10 inteiros e imprima a sua media
"""

num = 0
media = 0

for i in range(0, 10):
    num = float(input())
    media = media + num
media = media/10
print(f'{media}')

