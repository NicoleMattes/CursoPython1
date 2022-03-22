n = int(0)
valor = int(0)

while valor != 100000:
    for n in valor:
        valor = n+1000
        print(f'{valor}')
        if valor == 100000:
            print(f'{valor}')
            break
