from time import sleep


#O valor é entregue aos poucos em uma função geradora,economizando memoria
gerador = (x for x in range(100))
for x in gerador:
    print(x)
    sleep(0.1)    
    

cor = ['preto','branco']
tamanho = ['P','M','G']
for camisa in ('%s %s' %(c,t) for c in cor for t in tamanho):
    print(camisa)    
    
    
t=[1,2,3,4,5]
u=[1,2,3,4,5]    
prodCartesiano = ( (x,y) for x in t for y in u)
for valor in prodCartesiano:
    print(valor) 