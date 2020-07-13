###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 10/Jul/2020
###############################################

import aula7 #Importando um arquivo completo
if __name__ == "__main__":
    pass
    # tv1 = aula7.Televisao()
    # print(tv1.power)
    # print(tv1.canal)
    # tv1.btnLigaDesliga()
    # print(tv1.power)
    # print(tv1.canal)

from aula7 import Televisao #Importando uma classe

if __name__ == "__main__":
    pass
    # print('Televisão')
    # tv = Televisao()
    # print(tv.power)
    # print(tv.canal)
    # tv.btnLigaDesliga()
    # print(tv.power)
    # print(tv.canal)

from aula7 import Calculadora2 #Importando uma classe

if __name__ == "__main__":
    pass
    # print('\n\nCalculadora')
    # calc = Calculadora2()
    # a = 5.1
    # b = 7.3
    # print('Valor de A = {}'.format(a))
    # print('Valor de B = {}'.format(b))
    # soma = calc.soma(a,b)
    # print('A soma de A e B = {}'.format(soma))
    # subtracao = calc.subtracao(a,b)
    # print('A subtração de A e B = {}'.format(subtracao))
    # multiplicacao = calc.multiplicacao(a,b)
    # print('A multiplicação de A e B = {}'.format(multiplicacao))
    # divisao = calc.divisao(a,b)
    # print('A divisão de A e B = {}'.format(divisao))


from aula8_contador_letras import contador_letras, teste #Importando função ou método

if __name__ == "__main__":
    # lista = ['cachorro', 'gato', 'pato', 'lontra']
    # print('Lista: {}'.format(lista))
    # print('Lista com a quantidade de letras: {}'.format(contador_letras(lista)))
    # print(teste())

    contador_letras2 = lambda lista : [len(x) for x  in lista] #Função anonima (lambda)

    # print('Lista com a quantidade de letras: {}'.format(contador_letras2(lista)))

    #Funções lambda (calculadora)
    soma_ = lambda a,b: a+b
    subtracao_ = lambda a,b: a-b
    multiplicacao_ = lambda a,b: a*b
    divisao_ = lambda a,b: a/b

    a = 4
    b = 3
    # print('Valor de A = {}'.format(a))
    # print('Valor de B = {}'.format(b))
    # print('A soma de A e B = {}'.format(soma_(a,b)))
    # print('A subtração de A e B = {}'.format(subtracao_(a,b)))
    # print('A multiplicação de A e B = {}'.format(multiplicacao_(a,b)))
    # print('A divisão de A e B = {}'.format(divisao_(a,b)))

    #Funções lambda (calculadora) - Como lista
    calc_lambda = {
        'soma': lambda a,b: a+b,
        'subtracao': lambda a,b: a-b,
        'multiplicacao': lambda a,b: a*b,
        'divisao': lambda a,b: a/b,
    }

    # print('A soma de A e B = {}'.format(calc_lambda['soma'](a,b)))
    # print('A subtração de A e B = {}'.format(calc_lambda['subtracao'](a,b)))
    # print('A multiplicação de A e B = {}'.format(calc_lambda['multiplicacao'](a,b)))
    # print('A divisão de A e B = {}'.format(calc_lambda['divisao'](a,b)))
