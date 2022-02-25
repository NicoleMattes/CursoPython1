"""
Leia o salário de um trabalhador e o valor da prestação de se um empréstimo. Se a prestaçãp for maior que
20% do salário imprima: "Empréstimo n"ao concedido" caso contrário "Imprestimo concedido"
"""

print('Digite o valor do salário')
slr = float(input())

print('Digite o valor da parcela do imprestimo')
pcl = float(input())

if pcl > (slr*0.20):
    print('Empréstimo não concedido')

else:
    print('Empréstimo concedido')
