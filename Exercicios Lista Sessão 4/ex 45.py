"""
Faça um programa que converta uma letra minuscula em uma letra maiuscula, use a tabela ASCII para resolver o problema
"""

print("Digite uma letra em maisculo:")
mi = input()

cmi = ord(mi)

cmif = chr(cmi+32)

print(f'A letra minuscula é {cmif}')

