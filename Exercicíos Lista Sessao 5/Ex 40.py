"""
O custo ao consumidor de um carro novo é a soma do custo de fábricação, da comissão do distribuidor, e dos
impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo.
Leia o custo de fábrica e escreva o custo ao consumidor
    - Custo de fabrica: até 12.000,00 - % do distribuidor: 5 - % dos impostos: isento
    - Custo de fabrica: entre 12.000,00 e 25.000,00 - % do distribuidor: 10 - % dos impostos: 15
    - Custo de fabrica: acima de 15.000,00 - % do distribuidor: 15 - % dos impostos: 20
"""
valor_fabrica = float(input("Digite aqui o valor do carro de fábrica: \n"))

if valor_fabrica <= 12000:
    valor_fabrica = valor_fabrica * 1.05
    print(f"O valor do carro após o calculo de imposto é {valor_fabrica:.2f}")

elif 25000 >= valor_fabrica > 12000:
    valor_final = (valor_fabrica * 1.10) + (valor_fabrica * 0.15)
    print(f"O valor do carro após o calculo de imposto é {valor_final:.2f}")

elif 25000 < valor_fabrica:
    valor_final = (valor_fabrica * 1.15) + (valor_fabrica * 0.20)
    print(f"O valor do carro após o calculo de imposto é {valor_final:.2f}")