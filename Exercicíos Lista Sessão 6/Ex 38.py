"""
Faça um programa que calcule o termo pitagórico, 'a, b ,c' para o qual a+b+c = 1000. Um temo pitagórico é um conjunto
de três números naturais, a, b, c, para a qual
    a²  + b² = c²
ex
    3² + 4³ = 5²
    9 + 16 = 25
"""

# entrada das variaveis

a = int(input('Digite o valor de "a"\n'))
b = int(input('Digite o valor de "b"\n'))
c = int(input('Digite o valor de "c"\n'))
qa = int()
qb = int()
qc = int()

# processamento

qa = a*a
qb = b*b
qc = c*c

# saida

if qc == qa + qb:
    print('A enquação é pitagórica')
else:
    print('A equação não é piragórica')

