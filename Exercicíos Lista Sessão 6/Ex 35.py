"""
Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o valor
inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números impares contidos neste
intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior do que o valor final) deve ser
escrito uma mensagem de erro na tela "intervalo invalido" e o programa termina. Exemplo de tela de saida: "Digite o
valor inicial e valor final: e valor final 10 - Soma dos impares neste intervalo: 21
"""

# Entrada de dados:
# Intervalo deve ser definido pelo usuario através das variaveis A e B

a = int(input('Digite o unicio do intervalo numerico\n'))
b = int(input('Digite o fim do intervalo numerio\n'))
ip = int()
soma = int()

# Condição/validação Verificação se os valores digitados são validos

if a >= 0 or b < a:
    print('Os valores digitados são validos\n')
else:
    print('ERRO\n'
          'Um ou mais valores digitados não são validos\n')

# processamento - loop

for i in range(a, b+1):
    if i%2 == 1:
        soma = soma + i
print(f'A soma dos números impares é: {soma}')

