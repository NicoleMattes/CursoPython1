a = []

print('Digite 10 valors')
while len(a) < 10:
    x = int(input())
    a.append(x)
print(a)

m = max(a)
print(f'O maior elemento é: {m} e a sua possição é {a.index(m)}')
