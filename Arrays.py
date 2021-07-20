from array import array
from random import random

#Se a lista contiver somente numeros, um array será mais eficiente que uma lista
#ele aceita todas as operações de sequência mutáveis(pop,insert e extends) além de ter métodos 
#adicionais como carregar e salvar rapidamente por exemplo .frombytes e .tofile, entre outros

floats = array('d', (random() for i in range(10**7)))
# o argumento d é para criar um array do tipo double

print(floats[-1])

with open ('floats.bin','wb') as file:
    floats.tofile(file)
    
floats2 = array('d')

with open('floats.bin','rb') as file:
    floats2.fromfile(file,10**7)

print(floats2[-1])

print(floats[-1] == floats2[-1])

#Esse exemplo mostra que demora aproximadamente 0,1 segundo para carregar 10 millhoes do
#arquivo, isso é quase 60 vzes mais rápido que ler(.fromfile) números em um arquivo de texto
#Salvar(.tofile) é aproximadamente 7 vezes mais rápido que escrever um numero de ponto flutuante
#por linha em um arquivo de texto, além do tamanho do arquivo que passa ocupar apenas 8 bytes
#em vez de 181.515.739 bytes   