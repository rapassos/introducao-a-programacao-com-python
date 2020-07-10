#a = 10
#b = 5
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#print(type(soma))
resultado = (  'Soma: {soma}\n'
                'Subtração: {subtracao}\n'
                'Multiplicação: {multiplicacao}\n'
                'Divisão: {divisao}\n'
                'Resto: {resto}'.format(
                                        soma = soma,
                                        subtracao = subtracao,
                                        multiplicacao = multiplicacao,
                                        divisao = divisao,
                                        resto = resto))
print(resultado)
#print('Soma: ' + str(soma))
#print('Subtração:' + str(subtracao))
#print('Multiplicação: ' + str(multiplicacao))
#print('Divisão: '+ str(int(divisao)))
#print('Divisão: '+ str(divisao))
#print('Resto: '+ str(resto))
