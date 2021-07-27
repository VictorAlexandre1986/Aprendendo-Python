def fatorial(n):
    '''return n!'''
    return 1 if n < 2 else n * fatorial(n-1)

print(fatorial(5))

#atribuindo uma função a uma variavel
variavel = fatorial
print(variavel(3))

#passando uma função como parametro
print(list(map(fatorial,range(4))))

#Ordenando pelo tamanho das strings
fruits = ['apple','orange','cherry','banana','strawberry']
print(sorted(fruits, key=len))

#Invertendo a ordem das letras e ordenando as palavra em ordem alfabetica
def reverse (word):
    return word[::-1]
print(sorted(fruits,key=reverse))

#Funções com qtd variavel de argumentos
def soma(*args):
    acum=0;
    for i in args:
        acum += i

#É possível usar list comprehensions no lugar de map       
print([fatorial(n) for n in range(6)])
print([fatorial(n) for n in range(6) if n % 2 == 0])

print(list(map(fatorial,filter(lambda x:x % 2==0 , range(6)))))

#Não só funções Python são objetos reais, como também podemos fazer objetos
#Python quaisquer se comportarem como funções, basta implementar o metodo de instancia __call__

