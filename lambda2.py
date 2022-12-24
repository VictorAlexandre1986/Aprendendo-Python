
subtracao = lambda x, y: x - y


def executa(funcao, *args):
    return funcao(*args)

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return multiplicador * numero

    return multiplica


if __name__ == '__main__':
    print(subtracao(10, 2))

    acumulador= executa(lambda x, y: x + y, 2, 3)#lambda de soma
    print(acumulador)

    acumulador_2 = executa(lambda x: lambda y: x * y,2)#lambda da função multiplicador
    print(acumulador_2(3))

    print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8, 9))#lambda de soma com método sum