def divide(n1,n2):
    if n2 == 0:
        raise ValueError ('n2 não pode ser zero')
    return n1 / n2

try:
    divide(4,0)
except ValueError as error:
    print(error)
    print('Não foi possivel')