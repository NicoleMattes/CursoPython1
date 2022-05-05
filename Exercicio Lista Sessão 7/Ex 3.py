"""não permitir valores repetidos na lista"""

import math

l1 = []
l2 = []

while len(l1) < 10:
    x = float(input('digite um valor'))
    if x in l1:
        print('O valor não é valido')
    else:
        l1.append(x)
print(l1)

for i in l1:
    l2.append(math.sqrt(i))
print(l2)
