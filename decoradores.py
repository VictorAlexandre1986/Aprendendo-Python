from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} levou {tempo:.2f}ms, para ser executada.')
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)
        

demora()

#--------------------------------------------------------------------------------------
#Decorators serve para modificar funções sem precisar alterar a funcao em si , 
# mas adicionando funcionalidades
class uppercase:
    def __init__(self,funcao):
        self.funcao=funcao
        
    def __call__(self,*args):
        self.funcao(args[0].upper())
        

@uppercase
def nome(nome):
    print(f'Nome {nome}')


nome('victor')