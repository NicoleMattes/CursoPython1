"""
Mercado Livre - 13% + 5 reais por venda.
Mercado livre com frete grátis - Pedidos acima de R$ 79,00 - 13% + Frete, em média R$ 28,00
Shopee - 18% Frete grátis
Elo 7 - 13% ou 18%
"""

print('Valor sugerido de venda para Moldes.\n'
      'Por favor escolha uma das opções\n')

opc = 0

# opções

while 1 > opc or opc > 4:
    opc=int(input('1. Mercado Livre\n'
                  '2. Shopee\n'
                  '3. Elo7 \n '))

# Entrada de dados:

peso = float(input('Digite o peso do molde em KG\n'))
preco_kg =float(input('Digite o preço do KG em reais\n'))
embalagem = float(1)
frete_gratis_ml = float(27)

# processamento:

custo_da_peca = peso*preco_kg

venda_sem_taxa = (custo_da_peca*3)+embalagem

lucro = (venda_sem_taxa-custo_da_peca-embalagem)

# processamento e saida:

if opc == 1:
    valor_de_venda = ((venda_sem_taxa*0.13)+venda_sem_taxa+5)
    print(f'O preço de custo da peça é {custo_da_peca}\n'
          f'O lucro por venda é de R$ {lucro}\n'
          f'O valor recomendado de venda para a plataforme MERCADO LIVRE é de R$ {valor_de_venda}\n')

elif opc == 1 and venda_sem_taxa > 78.00:
    valor_de_venda = ((venda_sem_taxa*0.13)+venda_sem_taxa+5+frete_gratis_ml)
    print(f'O preço de custo da peça é {custo_da_peca}\n'
          f'O lucro por venda é de R$ {lucro}\n'
          f'O valor recomendado de venda para a plataforme MERCADO LIVRE com frete grátis é de R$ {valor_de_venda}\n')

elif opc == 2:
    valor_de_venda = ((venda_sem_taxa*0.18)+venda_sem_taxa)
    print(f'O preço de custo da peça é {custo_da_peca}\n'
          f'O lucro por venda é de R$ {lucro}\n'
          f'O valor recomendado de venda para a plataforme SHOPEE é de R$ {valor_de_venda}\n')

elif opc == 3:
    valor_de_venda1 = ((venda_sem_taxa*0.13)+venda_sem_taxa)
    valor_de_venda2 = ((venda_sem_taxa * 0.18) + venda_sem_taxa)
    print(f'O preço de custo da peça é {custo_da_peca}\n'
          f'O lucro por venda é de R$ {lucro}\n'
          f'O valor recomendado de venda para a plataforme ELO7 com baixa exposição é de R$ {valor_de_venda1}\n'
          f'O valor recomendado de venda para a plataforme ELO7 com alta exposição é de R$ {valor_de_venda2}\n')

else:
    print('O valor digitado é invalido')