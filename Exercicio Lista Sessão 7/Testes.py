
lista = [1, 2, 3, 'a', 'b', 'c']
lista2 = [20, 4, 2, 4]

lista.extend(lista2)

print(lista)

print(len(lista))

lista3 = 'Eu sou Palmeiras sim senhor e bebo todas que vier eu canto MEU PORCOOOOO OOOOOOH MEU UNICO AMOR DALE DALE DALE OOOOOOOH'
lista4 = lista3.split()

list1 = ['1', '2', '3', '4']

s = "-"
s = s.join(list1)
print(s)


lista6 = ['n', 'i', 'c', 'o', 'l', 'e', ' ', 'm', 'a', 't', 't', 'e', 's']

print(lista6)

print(type(lista6))

#somas das letas para foramr uma palavra, ou texto.
soma = ''
for i in lista6:
    print(i)
    soma = soma + i
print(soma)

cores = ['verde', 'amarelo', 'azul', 'branco', 'rosa', 'laranja']

for indice, cor in enumerate(cores):
    print(indice,cor)

print(cores.index('azul'))

print(sum(lista2))

lista5 = [1, 2, 3]
num1, num2, num3 = lista5
print(num1, num2, num3)


paises = {'br': 'Brasil', 'EUA': 'Estados Unidos da America', 'KO': 'Coreia do Sul'}
print('br' in paises)

del paises['br']
print(paises)

for chave in paises:
    print(chave)
for chave in paises:
    print(paises[chave])

from collections import namedtuple

cahorro = namedtuple("cachorro",['idade', 'raça', 'nome'])
print(f'{cahorro}')

ray = cahorro(idade=2, raça='chaw-chow', nome='Ray')
print(ray.nome)
