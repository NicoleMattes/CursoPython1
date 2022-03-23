"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número
de dados lidos e número de valores pares. O processo termina quando for digitado o número 1000
"""

n = int()
cont = 0
cont2 = 0

print('Digite os valores. 1000 encerra o programa')

while n != 1000:
    n = int(input())
    if n != 1000:
        cont = cont +1
    if n % 2 == 0:
        cont2 = cont2 +1
    if n ==1000:
        break
print(f'O número de dados recebido foi {cont}')
print(f'A quantidade de números pares é {cont2}')