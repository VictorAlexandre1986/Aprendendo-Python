#A função partial retorna uma funcao com seu argumento passado
#As funções parciais permitem derivar uma função com x parâmetros, para uma função com menos parâmetros e
# valores fixos definidos para a função mais limitada.

from functools import partial

def multiplicar(x,y):
    return x * y

multiplicado = partial(multiplicar,4)
print(multiplicado(2))


#A maneira manual de fazer abaixo
#A função soma congela o segundo argumento da função chamada funcao, o que resulta em uma nova função com uma assinatura
#mais simples.

#Em outras palavras, dsoma função reduz a complexidade da função função.

#Em Python, a função "funcao "é chamada de função parcial.

#Na prática, você usa funções parciais quando deseja reduzir o número de argumentos de uma função para simplificar a
# assinatura da função.

#Vai retornar um função com seu parametro passado, que poderá ser chamada usando parenteses e passando o
#argumento exigido na função retornada
def soma(x):
    def funcao(y):
        return x + y
    return funcao

resultado=soma(5)
print(resultado(5))


