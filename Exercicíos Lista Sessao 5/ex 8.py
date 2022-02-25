"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são validas e exiba na tela a média
destas notas. Uma nota Uma nota válida deve ser, obrigatóriamente, um valor entre 0.0 e 10.5, onde caso
a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa terminar.
"""

print('Digite as duas notas do aluno')
nota1 = float(input())
nota2 = float(input())

if nota1 >= 0 and nota2 >= 0:
    media = (nota1+nota2)/2
    print(f'A media é {media}')

else:
    print(f'Nota digitada é invalida')
