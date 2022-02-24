# Leia o salário de um funcionario. Calcule e imprima o valor do novo salario com aumento de de 25%

print('Digite o valor do salário (lembrando que o . é usado no lugar da virgula)' )
salario = float(input())
ns = salario+(salario*25/100)
print(f'O novo salario com aumento de 25% é R$ {ns}')