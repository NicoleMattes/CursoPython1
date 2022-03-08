"""
Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou 5 mas não
simultaniamente pelos dois
"""

num = int(input('Digite um número inteiro\n'))

while num % 3 == 0 and num % 5 == 0:
    num = int(input("Digite o numero novamente, pois esse numero é divisível por 3 e 5 \n"))

while num % 3 != 0 and num % 5 != 0:
    num = int(input("Digite o numero novamente, pois esse numero não é divisível por 3 ou 5 \n"))

if num % 3 == 0:
    print(f'O número informado é divisível por 3')
else:
    print(f'O número informado é divisível por 5')