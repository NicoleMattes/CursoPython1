"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as basicas, por exemplo)
O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e lealiza a operação,
mostrando o resultado e a saindo.
"""

print('Escolha uma das opções\n')
opc = 0

while 1 > opc or opc > 4:
    opc=int(input('1. Para somar digite 1\n'
                  '2. Para dividir digite 2\n'
                  '3. Para subtrair digite 3\n'
                  '4. Para mutiplicar digite 4\n'))

v1 = int(input('Digite o primeiro valor\n'))
v2 = int(input('Digite o segundo valor\n'))

if opc == 1:
    result =v1+v2
    print(f'O Resultado é {result}')

elif opc == 2:
    reult = v1/v2
    print(f'O resultado é {reult}')

elif opc == 3:
    result = v1-v2
    print(f'O resultado é {result}')

elif opc == 4:
    result = v1*v2

else:
    print('O número digita é invalido')
