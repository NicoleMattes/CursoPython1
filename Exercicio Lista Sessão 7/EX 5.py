a = []
i = 0
cont = 0


# Entrada de dados na lista

print('Digite 10 valores inteiros\n')
while len(a) < 10:
    x = int(input())
    a.append(x)
print(a)

# verificação dos pares

for i in range(0, len(a)):
    if i % 2 == 0:
        print(i)
        cont = cont + 1
print(cont)
