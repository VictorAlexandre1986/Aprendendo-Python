from functools import reduce

produtos = [
    {'nome':'p1', 'preco':10.10},
    {'nome':'p2', 'preco':13.25},
    {'nome':'p3', 'preco':29.12},
    {'nome':'p4', 'preco':45.04},
    {'nome':'p5', 'preco':5.38},
    {'nome':'p6', 'preco':17.59},
    {'nome':'p7', 'preco':31.70},
    {'nome':'p8', 'preco':21.45},
    {'nome':'p9', 'preco':59.19},
    {'nome':'p10', 'preco':2.12},
]

lista = [1,2,3,4,5,6,7,8,9]

soma_lista = reduce(lambda acumulador , item: item + acumulador, lista,0)
print(soma_lista)

soma_preco = reduce(lambda acumulador, produtos: produtos['preco']+ acumulador,produtos,0)
print(soma_preco)
media = round((soma_preco/len(produtos)),2)
print(f'Média {media}')