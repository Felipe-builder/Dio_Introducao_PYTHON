from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculora = Calculadora(5, 10)
    print(calculora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    print('total de letrpor palavra da lista: {}'.format(contador_letras(lista)))
    print(teste())
