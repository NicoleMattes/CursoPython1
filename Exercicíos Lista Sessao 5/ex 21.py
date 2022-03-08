"""
Escreva o menu de opções a baixo. Leia a opção escolhida pelo usuário e execute a operação escolhida. Escreva
uma mensagem de erro se a opção for invalida
Escolha a opção
    1. - Soma de 2 números
    2. - Diferença entre 2 números (maior pelo menor)
    3. - Produto entre 2 números.
    4. - Divisão entre 2 números (o denominador não pode ser zero)
"""

# Entrada de dados

print('Escolha uma das opções:')
opc = 0

while 1 > opc or opc > 4:
    opc = int(input('1. Soma de 2 números\n'
                    '2. Diferença entre 2 números (maior pelo menor)\n'
                    '3. Produto entre 2 números.\n'
                    '4. Divisão entre 2 números (o denominador não pode ser zero)\n'))

num1 = float(input('Digite um número\n'))
num2 = float(input('Digite outro número\n'))

if opc == 1:
    result = num1 + num2
    print(f'O resultado é {result}')

elif opc == 2:
    if num1 > num2:
        result = num1-num2
        print(f'O resultado é {result}')
    else:
        result = num2-num1
        print(f'O resultado é {result}')

elif opc == 3:
    result = num1*num2
    print(f'O resultado é {result}')

elif opc == 4:
    while num2 == 0:
        num2 = int(input('O num2 não pode ser 0. Digite o num2 novamente\n'))
        final = num1/num2
        print(f'O resultado é {final}')

else:
    print('O número é invalido')