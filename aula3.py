###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 10/Jul/2020
###############################################

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))

# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b >c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))

# print('Final do programa!!!')

#=================================================

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a%2
# resto_b = b%2

# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par!')
# else:
#     print('Nenhum numero par foi digitado!')

#=================================================

while True:
    a = float(input('Primeiro bimestre: '))
    b = float(input('Segundo bimestre: '))
    c = float(input('Terceiro bimestre: '))
    d = float(input('Quarto bimestre: '))
    if (a+b+c+d) <= 40 and (a+b+c+d) >= 0:
        break
    else:
        print('Valores inválidos!!! \n Tente novamente...')

media = (a + b + c + d) / 4
print('Média: {}'.format(media))
