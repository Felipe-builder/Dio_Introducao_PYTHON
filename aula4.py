a = int(input('Primeiro bimestre: '))
while a >= 10 or a < 0:
    a = int(input('Nota inválida: Entre com a nota: '))
b = int(input('Segundo bimestre: '))
while b >= 10 or b < 0:
    b = int(input('Nota inválida: Entre com a nota: '))
c = int(input('Terceiro bimestre: '))
while c >= 10 or c < 0:
    c = int(input('Nota inválida: Entre com a nota: '))
d = int(input('Quarto bimestre: '))
while d >= 10 or d < 0:
    d = int(input('Nota inválida: Entre com a nota: '))
media = (a+b+c+d)/4
print(media)


# nota = int(input('Entre com a nota: '))
# while 10 < nota < 0:
#     nota = int(input('Nota inválida: Entre com a nota: '))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# a = int(input('até que valor você deseja saber os primos? '))
# for number in range(a+1):
#     div = 0
#     for x in range(1, number+1):
#         # print(x, number % x)
#         if number % x == 0:
#             div += 1
#
#     if div == 2:
#         print('número {} é primo'.format(number))


# number = int(input('Entre com um número: '))
#
# div = 0
# for x in range(1, number+1):
#     print(x, number % x)
#     if number % x == 0:
#         div += 1
#
# if div == 2:
#     print('número {} é primo'.format(number))
# else:
#     print('número {} NÃO é primo'.format(number))
