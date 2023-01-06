import enum

#Declarando de maneira funcional
Direcoes = enum.Enum('Direcoes', ['CIMA', 'BAIXO', 'ESQUERDA', 'DIREITA'])


def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError("Direção inválida")

    print(f'1) Movendo para : {direcao}')
    print(f'2) Movendo para : {direcao.value}')
    print(f'3) Movendo para : {Direcoes(1)}')
    print(f'4) Movendo para : {Direcoes["DIREITA"]}')
    print(f'5) Movendo para : {Direcoes(1).name}')
    print(f'6) Movendo para : {Direcoes.DIREITA.value}')
    print(f'7) Movendo para : {direcao.name}')
    print(f'8) Movendo para : {Direcoes.DIREITA.name}')

mover(Direcoes.DIREITA)





#Declarando em forma de classe
class Direcao(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2
    CIMA = 3
    BAIXO = enum.auto #Atribui valor de maneira automatica

print(Direcao.DIREITA)


print(f'Numero de direções disponíveis : {len(Direcoes)}')

print(f'Lista reversa : {list(reversed(Direcoes))}')
