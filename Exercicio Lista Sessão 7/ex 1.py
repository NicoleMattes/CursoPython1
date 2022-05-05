a = []
while len(a) < 6:
    x = float(input('escreva um número:'))
    if x in a:
        print('não pode escrever esse número')
    else:
        a.append(x)

print(a)

soma = a[0] + a[1] + a[5]
print(soma)

a.insert(4, 100)
print(a)

for i in a:
    print(i)

print('\n'.join(map(str, a)))
