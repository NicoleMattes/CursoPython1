"""
Escreva um programa de ajuda para os vendedores, a partir de um valor liquido, mostre:
    - Total a pagar com 10% de desconto para pagamento a vista
    - O valor de cada parcela no parcelamento em 3x sem juros
    - A comissão do vendedor, no caso da venda ser a vista é de (5% sobre o valor com desconto)
    - A comissão do vendedor, no caso da venda ser a praso é de 5% sobre o valor total do produto.
"""

print('Digite o valor do produto')

p = float(input())
pv = p-(p*10/100)
print(f'O valor para pagamento a vista, com desconto de 10 é de R$ {pv}')

cv = pv-(pv*95/100)
print(f'O valor da comissão para o pagamento a vista é de R$ {cv}')

ppp = p/3
print(f'O valor de cada parcela é de {ppp}')

cp = p-(p*95/100)
print(f'O valor da comissão para a venda a parcelada é de R$ {cp}')
