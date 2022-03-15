"""
Faça um algoritmo que calcule o IMC de uma e mostre a sua classificação de acordo com a tabela abaixo
    - IMC: > 18,5 - classificação: abaixo do peso
    - IMC: 18,6 a 24,9 - classificação: saudavel
    - 25,0 a 29,9 - classificação: peso em excesso
    - 30,0 - 34,9 - classificação: obesidade grau 1
    - 35 - 39,9 - Obsidade Grau 2 (severa)
    - acima de 40 - Obsidade grau 3 (mórbida)
"""

altura = float(input("Digite sua altura"))
peso = float(input("Digite seu peso"))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print("Abaixo do peso")
elif 25 > imc > 18.5:
    print("Saudável")
elif 30 > imc >= 25:
    print("Peso em excesso")
elif 35 > imc >= 30:
    print("Obesidade grau 1")
elif 40 > imc >= 35:
    print("Obesidade grau 2 (severa)")
else:
    print("Obesidade grau 3 (morbida)")