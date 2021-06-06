from itertools import zip_longest


cidade = ['São Jose dos Campos','Jacareí','Caçapava']
estado = ['São Paulo','Minas Gerais','Paraná','Santa Catarina']

#Quando a qtd das listas não são iguais , a diferença é descartado
unindo =zip(cidade,estado)
unindo2 =zip(cidade,estado)

#Quando a qtd das listas não são iguais é preenchido com none usando zip_longest
unindo3= zip_longest(cidade,estado,fillvalue='Vazio')

for x in unindo:
    print(x)
    

print(dict(unindo2))


for x in unindo3:
    print(x)
    
