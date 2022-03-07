"""
A nota final de um estudante é calculada a partir de três notas atribuídas entrre o intervalo de 0 a 10,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média
das três notas mencionadas anteriormente obedece aos pesos:
    - Trabalho de laboatório: 2
    - Avaliação Semestral: 3
    - Exame final: 5
De acordo com o resultado mostre na tela se o aluno esta REPROVADO (media entre 0 e 2,9), DE RECUPERAÇÃO
(média entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias
"""

# Entrada de dados
aluno = str(input('Olá, qual o nome do Aluno?'))

print('Por favor, informe a nota do Trabalho de Laboratório')
ntl = float(input())

print('Por favor, informe a nota dda Avaliação Semestral')
nas = float(input())

print('Por favor, informe a nota do Exame Final')
nef = float(input())

# Processamento

media = ((ntl*2)+(nas*3)+(nef*5))/10

# Verificação e saida

if media <= 2.9:
    print(f'O {aluno} foi reprovado com a média {media} ')

elif 3 < media < 4.9:
    print(f'O {aluno} esta de Recuperação com a média de {media}')

else:
    print(f'O aluno {aluno} foi aprovado com média de {media} ')
