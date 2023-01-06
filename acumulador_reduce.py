from functools import reduce

if __name__=='__main__':
    lista=[
        {'produto': 'camiseta', 'preco': 19.32},
        {'produto': 'bermuda', 'preco': 42.12},
        {'produto': 'blusa', 'preco': 70.50},
        {'produto': 'jaqueta', 'preco': 215.00}
    ]

    def soma(acum, produto):
        acum += produto['preco']
        return acum

    acum = reduce(soma , lista, 0)
    print(acum)

#---------------------------------------------------

    total =''

    print(sum([p['preco'] for p in lista]))

#---------------------------------------------------

    total = reduce(lambda acum, lista: round(acum + lista['preco'], 2), lista, 0)
    print(total)




