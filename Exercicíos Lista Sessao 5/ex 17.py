"""
Faça um programa que calcule e mostre a área de um trapézio.
A = ((basemaior+basemenor)*altura)/2
"""

# Entrada de dados

bmaior = float(input('Digite o valor da Base Maior\n'))

bmenor = float(input('Digite o valor da base menor\n'))

altura = float(input('Digite o valor da Altura\n'))

# Processamento

area = ((bmaior+bmenor)*altura)/2

# Saida

print(f'A área do trapesio é {area}')