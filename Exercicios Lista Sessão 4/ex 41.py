"""
Faça um programa que leia o valor da hora trabalhada (em reais) e o quantidade de horas trabalhadas no mês.
Imprima o valor a ser do salario, adicionando 10% sobre o valor calculado
"""

print('Digite o valor da hora de trabalho (em reais)')
sh = float(input())
print('Digite a quantidade de horas trabalhadas (em horas)')
ht = float(input())
st = sh*ht
sf = st+(st*10/100)
print(f'O salario total é de R$ {sf}')