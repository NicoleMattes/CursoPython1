"""Sabendo que 'a' e 'b' são os catetos de um triângulo. Faça um programa que receba os valores de 'a' e 'b' e calcule o valor da hipotenusa e imprima o resultado desta operação. """

import math

print("Considerando 'a' e 'b' os catetos de um triangulo")
print("Digite o cateto 'A'")
a = float(input())
print("Digite o cateto 'B'")
b = float(input())
hip = math.sqrt(a ** 2 + b ** 2)

print(f"a hipotenusa é: {hip}")
