"""
Escreva um programa em Python que escreva na tela de 1 a 100, de 1 em 1, 3 vezes. Deve ser usando 'for' e 'while'
"""

qtd = 0

while (qtd < 3):
    for n in range (1, 10, 2):
        print(n)
        qtd = qtd + 1
    if qtd >= 3:
        break

