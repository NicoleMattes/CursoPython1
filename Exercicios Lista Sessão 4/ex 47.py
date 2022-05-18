"""
Leia um número inteiro de 4 dígitos  imprima cada digito em uma linha
"""

print('Digite um número de 4 dígitos')
num = float(input())
num = str(num)

print(f"primeiro digito é {str(num)[0]}")
print(f"segundo digito é {str(num)[1]}")
print(f"terceiro digito é {str(num)[2]}")
print(f"quarto digito é {str(num)[3]}")