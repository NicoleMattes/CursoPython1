"""
Escreva um programa que , dados os números inteiros, mostre na tela o maior deles, assim como a difereça
existente entre eles.
"""

print('Digite dois números (espaçados por enter)')
num1 = float(input())
num2 = float(input())

if num1 >num2:
    print(f'O número {num1} é maior que o {num2}')
    d1 = num1-num2
    print(f'A diferença entre eles é {d1}')

elif num2>num1:
    print(f'O número {num2} é maior que o {num1}')
    d2 = num2-num1
    print(f'A diferença entre eles é {d2}')

else:
    print(f'O numero {num1} e {num2} são iguais')