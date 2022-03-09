"""
Leia a distancia em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo
em km/l e escrema uma mensagem de acordo com a tabela abaixo
    - Menor que 8 km -> Venda o carro
    - entre 8 e 14 km -> Economico
    - Maior que 12 -> Super economico
"""

#Entrada de dados

dst = float(input('Por favor, digite a distancia em Km\n'))
l = float(input('Por favor, digite a quantidade de litros gastos\n'))

# Procesamento

km_hora = dst/l

if km_hora <= 8:
    print('Venda o carro!\n')

elif 8 <= km_hora <= 14:
    print('Ecônomico!\n')

elif km_hora > 12:
    print('Super Ecônomico\n')

else:
    print('Valor invalido\n')