###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 10/Jul/2020
###############################################

# a = int(input('Entre com um número: '))

# divisores = 0

# for x in range(2, a):
#     if (a % x) == 0:
#         divisores += 1

# if divisores > 0 :
#     print('{} não é primo.'.format(a))
# else:
#     print('{} é primo'.format(a))

#==================================================

print('Números primos:\nÉ todo número divisível apenas por 1 e por ele mesmo!!!')

a = int(input('Entre com um número e conheça todos os números primos até o valor digitado: '))

primos = ''
count_primos = 0
for n in range(1, a+1):
    divisores = 0
    for x in range(2, n):
        if (n % x) == 0:
            divisores += 1
            break

    if divisores == 0:
        primos += '{} '.format(n)
        count_primos += 1
        
print(
    'Os números primos são:\n'
    '{primos}\n'
    'Totalizando: {count_primos} números primos'
    .format(
        primos=primos,
        count_primos=count_primos)
      )


