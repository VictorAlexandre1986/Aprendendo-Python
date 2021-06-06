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

def maiores(produto):
    if produto['preco']>20:
        return True

nova_lista = filter(maiores,produtos)

for x in nova_lista:
    print(x)
    

def novo_campo(produto):
    if produto['preco']>30:
        produto['é_caro']=True
    return produto 

nova_lista2 = filter(novo_campo,produtos)

for x in nova_lista2:
    print(x)