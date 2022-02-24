"""Considerando a quantia de R$ 780.000,00 será divida em 3 ganhadores, sendo que
    - O primeiro ganhará 46% do valor
    - O Segundo ganhará 32% do valor
    - O terceiro ganhará o valor que sobrar
Calcule e imprima a quantia que cada um ganhará
"""

premio = 78000000
print(f'O valor do premio é {premio}')
pg = premio-(premio*54/100)
sg = premio-(premio*68/100)
tg = premio-pg-sg
print(f'O primeiro ganhador, ganhará {pg}')
print(f'O Segundo ganhador, ganhará {sg}')
print(f'O terceiro ganhador, ganhará {tg}')
