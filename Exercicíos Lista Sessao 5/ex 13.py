"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e segunda prova tem peso 1 e a
terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reporvado. A nota
deve ser igual ou superior a 60 pontos
"""

#Entrada de dados

print('Digite as notas dos Aluno')
n1 = float(input())
n2 = float(input())
n3 = float(input())

#procesamento

media = ((n3*2)+n1+n2)/4

#saída

if media >= 60:
    print(f'O aluno foi aprovado como a Média de {media}')

else:
    print(f'O aluno foi reprovado com média de {media}')
