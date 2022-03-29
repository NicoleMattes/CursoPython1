"""
Faça um programa que calcule a diferença entre a soma dos quadrados do primeiros 100 números e o quadrado da soma.
Ex a soma dos quadrados por 10 primeiros números naturais.
"""

#variaveis:

soma = int()
soma_dos_quadrados = 0
quadrado = int()
quadrado_da_soma = 0
dif = 0

# definir o intervalo
inc = int(input('Digite o começo do intervalo númerico \n'))
fim = int(input('Digite o ultimo número do intervalo \n'))

# processamento (fazer o quadrado da soma, e a soma dos quadrados)

for i in range(inc, fim+1):
    quadrado = i*i
    if quadrado > 0:
        soma_dos_quadrados = soma_dos_quadrados + quadrado
print(f'Soma dos Quadrados: {soma_dos_quadrados}')

for i in range(inc, fim+1):
    soma = soma + i
    quadrado_da_soma = soma * soma
print(f'O quadrado da soma é: {quadrado_da_soma}')

# diferença entre eles
if soma_dos_quadrados >= quadrado_da_soma:
    dif = soma_dos_quadrados - quadrado_da_soma
    print(f'A diferença entre eles é: {dif}')
else:
    dif = quadrado_da_soma - soma_dos_quadrados
    print(f'A diferença entre eles é de: {dif}')