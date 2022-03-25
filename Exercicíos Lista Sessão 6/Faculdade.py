"""
número divisivel por 3 e 5 ao mesmo tempo
"""


n = int(input())
if n % 3 == 0:
    if n % 5 ==0:
        print('O número é divisível por 3 e 5')
    else:
        print('O número não é divisível por 3 e 5')
else:
    print('O número não é divisível por 3 e 5')

