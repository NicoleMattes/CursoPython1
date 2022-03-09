"""
Determine se um determinado ano lido é bissexto. Sendo que um ano bissexto é dividido por 400 ou se for divisivel
por 4 e não for divisivel por 100. Por exemplo 1988, 1992, 1996
"""

ano = int(input('Digite o ano\n'))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")