###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 10/Jul/2020
###############################################

lista = [1, 3, 8, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista)
print(lista_animal)
print(lista_animal[1])

for x in lista_animal:
    print(x)

soma = 0
for x in lista:
    soma += x
print(soma)

print(sum(lista)) #Soma
print(max(lista)) #Maior valor
print(min(lista)) #Menor valor

novo_animal = 'lobo';
if novo_animal in lista_animal:
    print('{} já está na lista.'.format(novo_animal))
else:
    lista_animal.append(novo_animal)

print(lista_animal)

# lista_animal.pop()
# print(lista_animal)

# lista_animal.pop(1)
# print(lista_animal)

# lista_animal.remove('elefante')
# print(lista_animal)

lista.sort()
print(lista)
lista.reverse()
print(lista)


lista_animal.sort()
print(lista_animal)
lista_animal.reverse()
print(lista_animal)

tupla = (1, 10, 12, 14) #Não modifica
print(tupla)
print(tupla[2])

lista_numerica = list(tupla)
print(lista_numerica)

tupla_animal = tuple(lista_animal)
print(tupla_animal)

