a = []

print('Digite 6 valores pares')

while len(a) < 6:
    x = float(input())
    if x % 2 == 0:
        a.append(x)
    else:
        print('O valor digita do é invalido, tente novamente')
print(a)

a.reverse()

print(a)

