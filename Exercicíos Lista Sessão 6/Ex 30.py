"""
Faça um programa para calcular as seguintes sequências:
    --> 1 + 2 + 3 + 4 + 5 + ... + n
    --> 1 - 2 + 3 - 4 + 5 +...+ (2n - 1)
    --> 1  + 3 + 5 + 7 + ... + (2n - 1)
"""

S1 = 0
S2 = int()
S3 = int()
N = int(input())

for i in range(1, N+1):
    S1 = S1 + 1
print(f'S1 = {S1}')
for i in range(1,((2*N)-1)+1):
    if i%2 == 1:
        S2 = S2 + i
    if i%2 == 0:
        S2 = S2 - i
print(f'S2 = {S2}')
for i in range(1, ((2*N)-1)+1):
    if i%2 != 0:
        S3 = S3 + i
print(f'S3 = {S3}')
