"""
Escreva um programa que leia um número interio maior do que zero e devolva, na tela a soma de todos
os seus algoritimo. por exemplo, ao número 251 corresponderá o valor 8 (2+5 +1). Se o número não lido for
maior do que zero, o programa terminará com a mensagem "número inválido"
"""

num = int(input("Digite um numero \n"))
soma = 0

if num >= 0:
    for i in str(num):
        soma = int(i) + soma
    print(soma)
else:
    print("Numero menor que 0")