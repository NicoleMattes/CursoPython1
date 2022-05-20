"""
implemente um programa que calcula o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
"""

print('Olá! Por gentileza, com quem falo?')
nome = str(input())

print(f'Seja bem vindo(a) {nome}')
print(f'{nome} qual a sua idade?')
idade = int(input())

ano = 2022-idade
print(f'{nome} seu ano de nascimento é {ano}')
