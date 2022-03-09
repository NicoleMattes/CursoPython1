"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores que 100. Escolha
números aleatórios entre 1 a 100, e  mostrena tela a pergunta: "Qual é a soma de a + b, onde a e b são números
aleatórios. Peça a resposta. Faça cinco perguntas ao aluno e mostre para ele as perguntas e as respostas corretas,
alémde quantas vezes o aluno acertou
"""

from random import randint
count = 0
cert = 0

while count < 5:
    count = count + 1
    num1 = randint(0, 99)
    num2 = randint(0, 99)
    aResp = int(input(f"Pergunta de numero {count}. \n "
                      f"Digite abaixo a soma de {num1} + {num2} \n"))
    resp = (num1 + num2)
    if aResp != resp:
        print(f"Você errou, a soma de {num1} + {num2} é: {resp} \n")
        print(f"Você tem {cert} acertos")
    else:
        print(f"Você acertou! A soma de {num1} + {num2} é: {aResp} \n")
        cert = cert + 1
        print(f"Você tem {cert} acertos \n")