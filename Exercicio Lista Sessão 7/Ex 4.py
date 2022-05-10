a = []

while len(a) < 8:
    x = int(input('Digite um valor \n'))
    a.append(x)
print(a)

x = int(input('Digite um valor entre 0 e 7\n'))
y = int(input('Digite um valor entre 0 e 7\n'))

# soma dos valores

soma = a[x] + a[y]
print(soma)
print(a[x])
print(a[y])


