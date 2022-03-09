"""
Calcule as raízes da equação de 2° grau.
A variavel a tem que ser diferente de zero. Caso seja igual, imprima a mensagem 'não é equação de segundo grau'
    - Se Δ <0 não existe real. Imprima a mensagem 'não existe raiz'
    - SE Δ = 0 existe raiz real. Imprima a raiz e a mensagem 'raiz única'
    - Se Δ >= 0 imprima as duas raizes reais
"""

import math
a = float(input("informe o valor de A : \n"))
b = float(input("informe o valor de B : \n"))
c = float(input("informe o valor de C : \n"))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não Existe Raiz")
elif delta == 0:
    raizdelta = (-1 * b + (math.sqrt(delta)) / (2 * a))
    print(delta)
elif delta > 0:
    x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    x2 = (-1 * b - math.sqrt(delta) / (2 * a))
    print(f"as raizes são {x1},{x2}")