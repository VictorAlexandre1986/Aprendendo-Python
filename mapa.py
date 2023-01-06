if __name__=='__main__':
    lista=[
        {'produto': 'camiseta', 'preco': 19.32},
        {'produto': 'bermuda', 'preco': 42.12},
        {'produto': 'blusa', 'preco': 70.50},
        {'produto': 'jaqueta', 'preco': 215.00}
    ]

    def aumenta_dez_porcento(produto):
        produto['preco'] = round(produto['preco'] * 1.1, 2)
        return produto

    alterado = map(aumenta_dez_porcento,lista)
    #print(list(alterado)) exibe dentro de uma lista
    print(*list(alterado), sep='\n')#exibe fora da lista
    print('\n')

    alterado2 = map(lambda produto:round(produto['preco'] * 1.1, 2), lista)
    print(*dict(alterado2), sep='\n')


    #Feito de maneira programação funcional
    copia = [{**p, 'preco': round(p['preco'] * 1.1, 2)} for p in lista]
    print(copia)