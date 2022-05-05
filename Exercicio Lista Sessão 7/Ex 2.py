lista = []

while len(lista) < 6:
    x = float(input('Digite um valor:'))
    if x in lista:
        print('não pode escrever esse número')
    else:
        lista.append(x)
print(lista)