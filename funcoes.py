def var(msg):
    print(msg)
    
def dump():
    return var


variavel = dump()('oi')

def func(a1,a2,a3,nome='Victor'):
    return a1,a2,a3,nome

variaveis=func('1','2','3')

print(variaveis[3])


def func1(*args):
    print(*args)


func1(1,2,3,4,5)


lista=[1,2,3,4,5,6]

n1,n2,*n=lista

print(*n)

print(*lista)

def seila(*args):
    print(args)
    
seila(*lista,7)


def seila2(**kwargs):
    print(kwargs)
    
    idade = kwargs.get('idade')
    
    if idade is not None:
        print(idade)
    
    

seila2(nome="Victor",sobrenome="Alexandre",idade=33) 

  
