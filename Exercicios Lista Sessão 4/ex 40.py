"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo
encanador e imprima a quantidade liquida que deverá ser paga, sabendo-se que são descontados 8% para emposto de renda
"""

s = float(30)
print('Digite a quantidade de dias que o encanador trabalho')
d = float(input())
st = s*d
sf = st-(st*8/100)
print(f'O valor do salario final debitando o emposto de renda é de R$ {sf}')
