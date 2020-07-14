###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 13/Jul/2020
###############################################

#Divisão por 0
def testaDivisor(divisor):
    try:
        arquivo = open('teste.txt','r')
        texto = arquivo.read()
        divisao = 10/divisor
    except ZeroDivisionError:
        print('Impossível dividir por 0!!!')
    except IndexError:
        print('Indice inválido')
    else:
        print('Divisão ok')
        print(divisao)
        return divisao
    finally:
        print('Executa sempre na finalização do bloco "try"')
        arquivo.close()

#Indice inválido
def testaIndex(index):
    try:
        lista = [1,5]
        print(lista[index])
    except IndexError:
        print('Indice inválido')

#Variavel inexistente
def testaVariavel():
    try:
        a = 10
        x = a
        print(x)
        erroDesconhecido = [1]
        #erroDesconhecido[1]
        print(int(testaDivisor(0)))
    except NameError:
        print('Variável não definida')
    except TypeError:
        print('Tipo de dado incorreto, falha de conversão!!!')
    except BaseException as ex:
        print('Erro desconhecido.\nErro: {}'.format(ex))


class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


def excessoesPersonalizadas():
    while True:
        try:
            x = int(input('Entre com a nota: '))
            if x > 10 or x < 0:
                raise InputError('Entre com um valor de 0 a 10')
            break
        except ValueError:
            print('Valor inválido')
        except InputError as ex:
            print(ex)


if __name__ == "__main__":
    pass
    testaDivisor(0)
    testaDivisor(4)
    testaIndex(1)
    testaIndex(2)
    testaVariavel()
    excessoesPersonalizadas()