notas = []
numero_de_alunos = int(input('informe o número total de alunos \n'))

print('Informe as notas')

while len(notas) < numero_de_alunos:
    x = float(input())
    if x >= 0:
        notas.append(x)
    else:
        print('Nota Invalida')
print(notas)

soma = sum(notas)
media = soma / numero_de_alunos
print(f'A média da sala é {media}')

