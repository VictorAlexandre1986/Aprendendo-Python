l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

l2 = [variavel for variavel in l1]
print(l2)

l3 = [variavel * 2 for variavel in l1]
print(l3)
#----------------------------------------

l4 = [(x,y) for x in l1 for y in range(3)]
print(f'Coordenadas : {l4}')

#----------------------------------------
nomes = ['Victor','José','Rafaella','Maria']

ex = [nome.replace('a','@').upper() for nome in nomes]
print(ex)

#-----------------------------------------

tupla = (
    ('x','y'),
    ('x1','y1'),
)

ex2 = [ (y, x) for x, y in tupla]
print(f'Invertendo as posições originais : {ex2}')


#----------------------------------------
l5 = list(range(100))
l6 = [x for x in l5 if x % 2 == 0 if x % 3 ==0]
print(f'Numeros divisiveis por dois e três : {l6}')

#----------------------------------------
l7 = [v if v % 3 == 0 else 0 for v in l5]
print(f'Divisiveis por 3 : {l7}')