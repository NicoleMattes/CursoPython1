"""
Dados n e dois números inteiros positivos, A e J, diferentes de 0, imprima em ondem crescente os n primeiros naturais
que são múltiplos de i ou j de ambos. Exemplo: Para n = 6, i = 2 e j = 3 a saída deverá ser: 0, 2,3,6,8.
"""

# n -> determina o valor do intervalo
# a e j -> tem que ser multiplo de ambos

n = int(input('Digite um valor \n'))
a = int(input('Digite outro valor\n'))
j = int(input('Digite mais um valor\n'))
ma = 1
mj = 1

if n < 0 and a < 0 and j < 0:
    print('Um ou mais valores estão errados')
else:
    print('Os valores são validos')

for i in range(1, n+1):
    if i % a == 0:
        i % j == 0
        print(f'{i}')

