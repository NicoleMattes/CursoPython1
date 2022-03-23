"""
Escreva um algoritmo que leia certa quantidade de númerios e imprima o maior deles e quantas vezes o maior
número foi lido. A quantidade de números lidos devem ser dornecidas pelo usuatio
"""

qtd = int(input('Digite a quantidade de variáveis \n'))
num = 0
maior = float()
menor = float()
cont = 0

for i in range(0, qtd):
    num = float(input('Digite o valor da variável: '))
    if i == 0:
        maior = num
        menor = num
    if num == maior:
        cont = cont + 1
    if num > maior:
        maior = num
        cont = 1
    if num < menor:
        menor = num

print(f'maior:{maior}')
print(f'menor: {menor}')
print(f'O maior apareceu {cont} vezes')

