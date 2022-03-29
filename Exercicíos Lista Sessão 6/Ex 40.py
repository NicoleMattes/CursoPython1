"""
Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo
O programa tem que retornar o menor número lido
"""

num = int()
menor = int()

verify = True
cont = 0

while verify:
    num = float(input('Digite um valor \n'))
    if num > 0:
        menor = num
    if num > menor:
        menor = num
    if num <= 0:
        verify = False
print(f'menor: {menor}')

