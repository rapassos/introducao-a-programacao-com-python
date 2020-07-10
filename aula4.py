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

a = int(input('Entre com um número: '))

primos = 'Primos: '
for n in range(1, a+1):
    divisores = 0
    for x in range(2, n):
        if (n % x) == 0:
            divisores += 1
            break

    if divisores == 0:
        primos += '{} '.format(n)
print(primos)