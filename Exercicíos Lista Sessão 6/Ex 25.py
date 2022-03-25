"""
Faça um program que some todos os números naturais abaixo de 1000 que são multiplos de 3 ou 5
"""

cont = 0
soma3 = 0
soma5 = 0

for i in range(0, 1000):
    if i % 3 == 0:
        soma3 = soma3 + i
    if i % 5 == 0:
        soma5 = soma5 + i
print(f'A soma de todos os números naturais que são multiplos de 3 é {soma3}')
print(f'A soma dos números natuais multiplos de 5 é {soma5}')

