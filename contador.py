from itertools import count

contador = count(start=1,step=1)
lista=['A','B','C','D','E']
lista = zip(contador,lista)
print(list(lista))

contador = count(start=1,step=1)
for valor in contador:
    if valor == 10:
        break
    print(valor)