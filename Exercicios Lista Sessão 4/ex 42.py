"""
Receba o valor do salario base de um funcionário. Calcule e imprima o salario a receber, sabenod que esse funcionário
tem uma gratificação de 5% sobre o salario base. Além disso ele paga 7% em impostos sobre o salario base
"""

print('Digite o valor do salario-bade do funcionario  (em reais)')
sb = float(input())
st = sb+(sb*5/100)
sf = st-(st*7/100)
print(f'O Salário é de R$ {sf}')
