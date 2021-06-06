from itertools import count

lista = ['Victor','Alexandre','Braga','Ribeiro']

contador = count(start=2,step=2)

for x in contador:
    print(x)
    if x == 20:
        break
    

lista2=zip(contador,lista)
for x in lista2:
    print(x)
    
        
    