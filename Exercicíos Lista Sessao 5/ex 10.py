"""
Faça um programa que receba a altura e o sexo de uma pessoa e mostre seu peso ideal.
Utilizando as seguintes formas (onde h corresponde a alteura):
    - Homens: (72*h)-58
    - Mulheres: (62,1*h)-44,7
"""

print('Qual o seu gênero?'
      'Digite 1 para feminino \n'
      'Digite 2 para Masculino \n')
g = float(input())

print('Qual a sua altura? (em metros)')
h = float(input())

if g == 1:
    pi = (62.1*h)-44,7
    print(f'A altura ideal é {pi}')

else:
    pi2 = (72.7*h)- 58
    print(f'A altura idela é {pi2}')
