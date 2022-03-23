"""
Escreva um programa completo, que permita a qualquer aluno introduzir, pleo teclado, uma sequência arbitrário de notas
(válidas no inttervalo de 10 a 20) e que mostre na tela, como resultado, a correspondene média aritimética. O número
de notas com o que o aluno pretende efetuar o calculo não será fornecido ao programa, o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação.
"""

# notas só são validas entre 10 e 20
# encerra ao digitar nota não valida
# media = soma das notas / contado de quantas notas

notas = float()
cont = int()
soma = 0
media = float()
print('Digite as notas\n'
      'As notas valiadas são entre 10 e 20\n'
      'para fializar o programa digite uma nota invalida\n')

while 10 <= notas or notas <= 20:
    notas = float(input())
    if 10 <= notas and notas <= 20:
        print('Nota Valida')
        cont = cont + 1
        soma = soma + notas
        media = soma % cont
    if 10 > notas or notas > 20:
        media = soma / cont
        break



print(f'A media é {media}')
print(f'A quantidade de notas digitadas foi {cont}')
