from functools import partial


lista = [{"produto":"camisa", "preco":25},
         {"produto":"bermuda", "preco":38},
         {"produto":"blusa", "preco":75},
         {"produto":"jaqueta", "preco":150},
         {"produto":"bota", "preco":330}]

#Método 1

novo_precos = [{**p, 'preco':p['preco']*1.1} for p in lista]

#---------------------------------------------------------------------

#Método 2

novo_precos_2 = [round(p['preco']*1.1,2) for p in lista]

#-----------------------------------------------------------------------

#Método 3

def calcula_porcentagem(produto,porcentagem):
    return round(produto['preco']*porcentagem,2)

novo_precos_3 = [{**p,'preco': calcula_porcentagem(p,1.1)} for p in lista]

print(novo_precos)
print(novo_precos_2)
print(novo_precos_3)

#----------------------------------------------------------------------------

#Método 4

def calcula_porcentagem_2(valor,percentual):
    return round(valor*percentual,2)

#Usando partial para criar clousure
dez_porcento = partial(calcula_porcentagem_2,percentual=1.1)

novo_precos_4 = [{**p, 'preco': dez_porcento(p['preco'])} for p in lista]

print(novo_precos_4)

#-----------------------------------------------------------------------------

#Método 5

def funcao_decoradora(funcao):
    def calcula_porcentagem01(valor,percentual):
        resultado = round(valor * percentual, 2)
        return resultado
    return calcula_porcentagem01

@funcao_decoradora
def teste(valor,porcentagem):
    return round(valor*porcentagem,2)


novo_precos_5 = [{**p, 'preco':teste(p['preco'],1.1)} for p in lista]

print(novo_precos_5)
#--------------------------------------------------------

#Método 6

novo_precos_6 = list(map(lambda x:round(x['preco']*1.1,2),lista))
print(novo_precos_6)
#----------------------------------------------------------

#Método 7

def calcular_porcentagem_2(valor):
    valor['preco'] = round(valor['preco']*1.1,2)
    return valor

novo_precos_7 = list(map(calcular_porcentagem_2,lista))

print(novo_precos_7)


