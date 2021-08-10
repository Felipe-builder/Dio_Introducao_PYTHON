lista = [1, 31, 21, 7, 0]
lista_animal = ['cachorro', 'gato', 'elefante', 'cavalo']
print(lista_animal[1])
lista_animal[1] = 'macaco'
print(lista_animal[1])

for x in lista_animal:
    print(x)

soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)

print(sum(lista))
print(max(lista))
print(max(lista_animal))
print(min(lista_animal))
nova_lista = lista_animal * 3
print(nova_lista)

search = 'lobo'
if search in lista_animal:
    print('existe um {} na lista'.format(search))
else:
    print('Não existe um {a} na lista. {a} será incluído na lista'.format(a=search))
    lista_animal.append(search)
print(lista_animal)
# lista_animal.pop()
# print(lista_animal)
# lista_animal.pop(1)
# print(lista_animal)
# lista_animal.remove('elefante')
# print(lista_animal)
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica= list(tupla)
print(type(lista_numerica))
print(lista_numerica)
