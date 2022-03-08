"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem
, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceiotos:
    - O comprimento de cada lado de um triângulo é menor do que a soma dos outros lados.
    - Chama-se equilátero o triângulo que tem Trr^s lados iguais.
    - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
    - Recebe o nome de esclano o triängulo  que tem os trës lados diferentes.
"""

# entrada de dados

a = int(input('Digite um valor\n'))
b = int(input('Digite um valor\n'))
c = int(input('Digite um valor\n'))

# Processamento

while b + c < a:
    print('O valor inserido em "A" não pode ser maior do que a soma de "B" + "C", digite novamente')
    a = int(input('Digite o lado A de um triângulo\n'))
    b = int(input('Digite o lado B de um triângulo\n'))
    c = int(input('Digite o lado C de um triângulo\n'))

while a + c < b:
    print('O valor inserido em "A" não pode ser maior do que a soma de "A" + "C", digite novamente')
    a = int(input('Digite o lado A de um triângulo\n'))
    b = int(input('Digite o lado B de um triângulo\n'))
    c = int(input('Digite o lado C de um triângulo\n'))

while b + a < c:
    print('O valor inserido em "A" não pode ser maior do que a soma de "B" + "A", digite novamente')
    a = int(input('Digite o lado A de um triângulo\n'))
    b = int(input('Digite o lado B de um triângulo\n'))
    c = int(input('Digite o lado C de um triângulo\n'))

if a == b == c:
    print("O triangulo é equilatero")

elif a == b != c or a == c != b or c == b != a:
    print("O triangulo é isosceles")

else:
    print("O triangulo é escaleno")
