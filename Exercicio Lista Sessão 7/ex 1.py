



v = []
while len(v) < 10:
    x = int(input("Escreva um numero: "))
    if x in v:
        print("Nao pode escrever esse numero.")
    else:
        v.append(x)

print(v)
