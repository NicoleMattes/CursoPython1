"""
Faça um programa que calcule o menor número divisivel por cada um dos números de 1 a 20
Ex: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""

# intervalo = entre 1 a 20
# multiplo comum

verify = True
cont = 1
while verify:
    if cont % 1 == 0 and cont % 2 == 0 and cont % 3 == 0 and cont % 4 == 0 and cont % 5 == 0 and cont % 6 == 0 \
            and cont % 7 == 0 and cont % 8 == 0 and cont % 9 == 0 and cont % 10 == 0 and cont % 11 == 0 \
            and cont % 12 == 0 and cont % 13 == 0 and cont % 14 == 0 and cont % 15 == 0 and cont % 16 == 0 \
            and cont % 17 == 0 and cont % 18 == 0 and cont % 19 == 0 and cont % 20 == 0:
        print(f'{cont}')
        verify = False
    else:
        cont = cont + 1