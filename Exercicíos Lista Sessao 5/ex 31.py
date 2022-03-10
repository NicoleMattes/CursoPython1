"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique
e mostre qual é a classificação dessa pessoa.
    - A -> Menor que 1,20 até 60kg
    - B -> De 1,20m a 1,70m até 60kg
    - C -> Maior de 1,70m até 60kg
    - D -> Menor que 1,20 entre 60 a 90kg
    - E -> De 1,20m a 1,70m entre 60 a 90kg
    - F -> Maior de 1,70m até entre 60 e 90kg
    - G -> Menor que 1,20 entre acima de 90kg
    - H -> De 1,20m a 1,70m entre  acima de 90kg
    - I -> Maior de 1,70m acima de 90kg
"""

a = float(input('Qual a altura?\n'))
p = float(input('Qual o peso?\n'))

if a <= 1.20 and p <= 60:
    print('Classificação A')

elif 1.20 <= a < 1.7 and p >=60:
    print('Classificação B')

elif a >= 1.7 and p >= 60:
    print('Classificação C')

elif a <= 1.20 and 60 <= p > 90:
    print('Classificação D')

elif 1.20 <= a < 1.7 and p > 90:
    print('Classificação E')

elif a >= 1.7 and p >= 90:
    print('Classificação F')

elif a <= 1.20 and  p > 90:
    print('Classificação G')

elif 1.20 <= a < 1.7 and p > 90:
    print('Classificação H')

elif a >= 1.7 and p >= 90:
    print('Classificação I')

else:
    print('Valor(es) digitados são invalidos')
