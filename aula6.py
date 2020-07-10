###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 10/Jul/2020
###############################################


conjunto = {1, 2, 3, 4, 4, 2, 4}
print(type(conjunto))
print(conjunto)

conjunto.add(5)
print(conjunto)

conjunto.discard(2)
print(conjunto)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
print('Conjunto 1: {}'.format(conjunto1))
print('Conjunto 2: {}'.format(conjunto2))

conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_diferenca1 = conjunto1.difference(conjunto2)
print('Diferença entre o conjunto 1 e 2: {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre o conjunto 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diferenca_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
print('Conjunto A: {}'.format(conjunto_a))
print('Conjunto B: {}'.format(conjunto_b))

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))

conjunto_subset = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}'.format(conjunto_subset))

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é superconjunto de B: {}'.format(conjunto_superset))

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}'.format(conjunto_superset))

lista_animais = ['cachorro', 'cachorro', 'gato', 'elefante', 'gato']
print('Lista de animais: {}'.format(lista_animais))
conjunto_animais = set(lista_animais)
print('Conjunto de animais: {}'.format(conjunto_animais))
lista_animais = list(conjunto_animais)
print('Lista de animais: {}'.format(lista_animais))


