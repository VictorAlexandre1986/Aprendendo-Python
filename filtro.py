if __name__=='__main__':
    lista=[
        {'produto': 'camiseta', 'preco': 19.32},
        {'produto': 'bermuda', 'preco': 42.12},
        {'produto': 'blusa', 'preco': 70.50},
        {'produto': 'jaqueta', 'preco': 215.00}
    ]

    def filtro(produto):
        return produto['preco'] >= 50

    selecionados = filter(filtro,lista)
    print(*list(selecionados), sep='\n')



    selecionados2 = [prod for prod in lista if prod['preco'] >= 50]
    print(selecionados2)





    vetor = list(range(1,50,1))

    def multiplos(valor):
        return valor % 5 == 0

    multiplos = filter(multiplos, vetor)

    print(list(multiplos))