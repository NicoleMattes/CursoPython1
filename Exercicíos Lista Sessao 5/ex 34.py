"""
Leia a nota e o número de faltas de um aluno, escreva seu conceito de acordo com a tabela abaixo, quanod o
aluno tem mais de 20 faltas ocorer a redução do conceito
    - Nota 9.0 até 10.0 - Conveito A - Conceito (mais de 20 faltas) B
    - Nota 7.5 até 8.9 - Conveito B - Conceito (mais de 20 faltas) C
    - Nota 5.0 até 7.4 - Conveito C - Conceito (mais de 20 faltas) D
    - Nota 4.0 até 4.9 - Conveito D - Conceito (mais de 20 faltas) E
    - Nota 0.0 até 3.9 - Conveito E - Conceito (mais de 20 faltas) E
"""

nota = float(input('Digite a nota do aluno\n'))
falta= int(input('Digite a quantidade de faltas do aluno\n'))

if 9.0 <= nota <= 10.0:
    if falta < 20:
        print('A')
    else:
        print('B')

elif 7.5 <= nota <= 8.9:
    if falta < 21:
        print("CONCEITO B")
    else:
        print("CONCEITO C")

elif 5 <= nota <= 7.4:
    if falta < 21:
        print("CONCEITO C")
    else:
        print("CONCEITO D")

elif 4 <= nota <= 4.9:
    if falta < 21:
        print("CONCEITO D")
    else:
        print("CONCEITO E")

else:
    print("CONCEITO E")
