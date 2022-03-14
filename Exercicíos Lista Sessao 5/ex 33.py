"""
Um produto vai sofrer um aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva
o preço novo, e escreva uma mensagem em função do preço novo (de acordo com os dados abaixo)
    - Preço antigo até R$ 50,00, percentual de aumento 5%
    - Preço antigo entre R$ 50,00 a R$ 100,00, percentual de aumento 10%
    - Preço antigo acima R$ 150,00, percentual de aumento 15%
    PREÇO NOVO
    - até R$ 80,00 Mensagem "barato"
    - entre R$ 80,00 e R$ 120,00 Mensagem "normal"
    - até R$ 120,00 eR$ 200,00 Mensagem "Caro"
    - acima de R$ 200,00 Mensagem "Muito caro"
"""

valor_antigo=float(input('Digite o valor do produto\n'))

if valor_antigo > 50:
    novo_valor=valor_antigo+(valor_antigo*0.05)


elif 50 < valor_antigo < 100:
    novo_valor = valor_antigo + (valor_antigo * 0.1)

else:
    novo_valor = valor_antigo + (valor_antigo * 0.15)

print(f'O novo preço do produto é {novo_valor:.2f}')

if novo_valor < 81:
    print('Barato')

elif 81 < novo_valor < 120:
    print('Normal')

elif 120 < novo_valor < 200:
    print('Caro')

else:
    print('Muito Caro')
