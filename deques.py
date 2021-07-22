from collections import deque

dq = deque(range(10),maxlen=10)
print(dq)

dq.rotate()
print(f'Pega o ultimo elemento e inverte sua posição : {dq}')

dq.rotate(5)
print(f'Invertendo cinco elementos {dq}')

#Se adicionar um elemento e extrapolar a quantia do deque, em uma ponta o valor será inserido
#e na outra será removido
#deque pode considerar inicio qualquer uma das pontas
dq.append(25) #inserindo na ponta direita
print(f'Adicionando um elemento {dq}')

dq.appendleft(12)#Inserindo na ponta esquerda

dq.extend([11,22,33])
print(dq)
dq.extendleft([10,20,30,40])
print(dq)

dq1 = deque(range(10,20), maxlen=10)

print(f'Verificando se o valor está presente {12 in dq1}')

print(f'Conta as ocorrencias em um deque :{dq.count(15)}')

#Copia rasa
copia = dq.copy()

dq.remove(40)
print(f'Removendo um elemento do deque : {dq}')

print(f'Obtendo o item atraves do indice : {dq[2]}')

try:
    print(f'Encontra a posição do intem informado {dq.index(7)}')
except:
    print('Esse valor não está no deque')
    
print(f'Removendo o elemento da ponta direita {dq.pop()}')
print(f'Removendo o elemento da ponta esquerda {dq.popleft()}')

print(f'Invertendo a ordem {dq1.reverse( )}')















