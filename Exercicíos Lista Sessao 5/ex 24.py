"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto
sobre o produto. (MG: 7%, SP 12%, RJ 15%, MS 8%).
Faça um programa em que o usuário entre com o valor e o estado de destino do produto e o programa retorne
o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado for invalido,
mostre uma mensagem de erro.
"""

print('Por favor escolha qual estado deve ser enviado o produto:\n')

opc = 0

#opções

while 1 > opc or opc > 4:
    opc=int(input('1. MG (Minas Gerais)\n'
                  '2. SP (São Paulo)\n'
                  '3. RJ (Rio de Janeiro\n'
                  '4. MS (Mato Grosso)\n'))

while 4 < opc or opc < 1:
    print('O múmero digitado não é valido. Digite novamente uma das opções abaixo\n \n')
    opc=int(input('1. MG (Minas Gerais)\n'
                  '2. SP (São Paulo)\n'
                  '3. RJ (Rio de Janeiro\n'
                  '4. MS (Mato Grosso)\n'))
