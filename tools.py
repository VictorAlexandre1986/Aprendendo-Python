from itertools import accumulate
from itertools import chain
from itertools import compress
from itertools import dropwhile
from itertools import filterfalse
from itertools import islice
from itertools import starmap


lista = [1,2,3,4,5,6,7,8,9]

#Vai somando os elementos sucessivamente
print(list(accumulate(lista, initial=1)))
print(list(accumulate(lista,lambda x, y : x * 1.05 + y )))
print(list(accumulate(lista, initial=100)))


#Concatena dois iteraveis
lista2 = [10,11,12,13,14,15,16,17,18,19]
print(list(chain(lista,lista2)))

#Retorna os valores da lista que possuem correspodente como True na outra lista
print(list(compress(lista,[1,1,1,0,0,0,1,1,1,0])))

#Elimina os elementos que retornam True para a condição
print(list(dropwhile(lambda x : x < 5, lista)))

#Elimina tudo que é falso
print(list(filterfalse(lambda x : x % 2 , lista)))

#Separa uma fatia
print(list(islice(lista,2,7)))


print(list(starmap(pow,[(2,5),(3,2)])))