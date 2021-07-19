#As tuplas pode ser usadas como registros ou como listas imutaveis

nome, cidade, estado,  pais = ('Victor','São José dos Campos','SP','Brasil')

coordenadas = (33.9425, -118.4058)

passagens = [('BRA','CE342567'),('USA','31195855'),('ITA','XDA205856')]

for passagem in passagens:
    print('%s/%s' % passagem)

print('#'*50)

for passagem in passagens:
    print(passagem[0], passagem[1])
    
print('#'*50)

for nacao, id in passagens:
    print(nacao,id)

print('#'*50)

#A função collections.namedtuple é uma factory que gera subclasses de tupla melhoradas
#com nomes de campos e nome de classe.
#Dois parametros são necessários para criar uma tupla nomeada:um nome de classe e uma 
# lista de nomes de campos,é possível acessar o campo pelo nome ou posicao
from collections import namedtuple
City = namedtuple('City','name country population coordinates')
SJC = City('São jose dos Campos','BRA', 680.000,(35.689722,139.691667))
print(SJC)

#Usando tuplas como lista imutaveis
valores = (1,2,3,4,5)
valores2 = (6,7,8,9)
print(valores + valores2) #concatenação
print(2 in valores)       #Verifica se contém
print(valores.count(1))   #Conta qts vezes o valor está presente
print(len(valores))       #Conta a qtd de elementos
print(valores[2])         #Pega o valor na posicao informada
print(valores2.index(6))  #Pegando o indice do valor
print(valores * 2)