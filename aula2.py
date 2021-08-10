a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
soma = str(soma)
print(type(soma))
print('soma: ' + soma)
print('subtração: ' + str(subtracao))
print('multiplicacao: {}'.format(multiplicacao))
print(type(divisao))
print('Divisão: {div} \n Resto: {res}'
      .format(div=divisao,
              res=resto))
# print(resto)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)
