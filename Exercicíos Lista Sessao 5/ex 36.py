"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor.
Para calcular a comissão, considere a tabela a baixo
    - Maior ou igual a R$ 100.000,00 - Comissão R$ 700,00 + 16% das vendas
    - Menor que 100.000,00 e maior ou igual a R$ R$ 80.000,00 - Comissão R$ 650 + 14%
    - Menor que 80.000,00 e maior ou igual a R$ R$ 60.000,00 - Comissão R$ 600 + 14%
    - Menor que 60.000,00 e maior ou igual a R$ R$ 40.000,00 - Comissão R$ 550 + 14%
    - Menor que 40.000,00 e maior ou igual a R$ R$ 20.000,00 - Comissão R$ 500 + 14%
    - Menor que 20.000,00 Comissão R$ 450 + 14%
"""
men = float(input("Digite o valor de vendas mensal \n"))

if men >= 100000:
    com = 700 + (men * 0.16)
    print(f"O valor da comissão é: R${com:.2f}")

elif 100000 > men >= 60000:
    com = 650 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")

elif 80000 > men >= 60000:
    com = 600 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")

elif 60000 > men >= 40000:
    com = 550 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")

elif 40000 > men >= 20000:
    com = 500 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")

else:
    com = 400 + (men * 0.14)
    print(f"O valor da comissão é: R${com:.2f}")