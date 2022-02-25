"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais
imprima a mensagem "números iguais"
"""

print('Digite dois números')
num1 = float(input())
num2 = float(input())

if num1 > num2:
    print(f'O número {num1} é maior que o {num2}')

elif num2 > num1:
    print(f'O número {num2} é maior que o {num1}')

else:
    print('Os dois números são iguais')
