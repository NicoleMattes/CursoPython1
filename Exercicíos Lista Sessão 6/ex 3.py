"""
Faça um algorito utilizando o comando while que mostre uma contagem regressiva de 10 a 0, terminando em 0. Que mostre
a mensagem 'FIM' após a contagem.
"""


numbers = list(range(10, -1, -1))
print(numbers)
print('fim')


# de outra maneira

cont = 10
while cont >= 0:
    print(f'{cont}')
    cont = cont -1
print('FIM')