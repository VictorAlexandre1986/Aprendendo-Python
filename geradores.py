import sys
import time

lista = list(range(1000))

#Tamanho da lista
print(sys.getsizeof(lista))

def gerador():
    for n in range(10):
        yield(n)
        time.sleep(0.1)
        
g = gerador()

#Verificando se é um gerador 
print(f"É um gerador ? {hasattr(g,'__next__')}")

#Utilizando um gerador 
print('Usando o método next ',next(g))

#Utilizando um gerador
for x in g:
    print(x)
    
def gerador2():
    variavel="valor 1"
    yield(variavel)
    variavel="valor 2"
    yield(variavel)
    variavel="valor 3"
    yield(variavel)
    
for x in gerador2():
    print(x)
    
y = gerador2()

for x in y:
    print(x)
    
#criando gerador
gera = (x for x in range(10000))

#Tamanho do gerador
print(f'Tamanho do gerador é : {sys.getsizeof(gera)} bytes')


nome="Victor Alexandre Braga Ribeiro"
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))