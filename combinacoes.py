from itertools import combinations,permutations,product

lista = ['Victor','Alexandre','Braga','Ribeiro']

#A ordem não importa
for grupo in combinations(lista,2):
    print(grupo)

print('#'*50)

#A ordem importa, os valores não se repetem
for grupo in permutations(lista,2):
    print(grupo)

print("#"*50)

#A ordem importa e os valores se repetem
for grupo in product(lista,repeat=2):
    print(grupo)
