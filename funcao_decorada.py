def decoradora(funcao):
    print("Estou na função decorada")
    def aninhada(*args, **kwargs):
        print("Aninhada")
        resultado = funcao(*args,**kwargs)
        return resultado
    return aninhada


@decoradora
def soma(x,y):
    return x + y
#------------------------------------------------------------------

def criar_funcao(func):
    def interna(*args,**kwargs):
        for arg in args:
            e_string(arg)
        resultado= func(*args, **kwargs)
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(valor):
    if not isinstance(valor, str):
        raise TypeError("Valor deve ser uma string")


invertida = inverte_string("123")
print(invertida)
#------------------------------------------------------------------
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)


def multiplica(multiplicador):
    def calcula(valor):
        return multiplicador * valor
    return calcula


dois_vezes_tres = multiplica(3)
print(dois_vezes_tres(2))