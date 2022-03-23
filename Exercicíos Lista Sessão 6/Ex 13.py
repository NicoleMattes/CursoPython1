"""
Faça um program que leia um número inteiro positivo par N e impria todos os númeors pares de 0 até N em ordem
crescente
"""


n = float(input('Digite um número\n'))
while n < 0 or n % 2 == 1:
    print('Número invalido')
    n = float(input('Digite um número par\n'))

for i in range(0, int(n) + 1):
    if i % 2 == 0:
        print(f'{i}')


# descobrir pq o while não deu certo