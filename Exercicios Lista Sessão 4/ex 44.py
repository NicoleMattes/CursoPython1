"""
Receba a altura do degrau de uma escada e a altura que o usuário pretende alcançar subindo a escada. Calcule e
mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""

print('Qual é a altura dos degrais da escada?')
d = float(input())

print('Qual a altura que o usuário gostaria de subir? (em centimentros)')
a = float(input())

qd = a/d
print(f'A quantidade de degraus é de {qd}')

