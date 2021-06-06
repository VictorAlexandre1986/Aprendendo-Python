t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'Victor')

t2= tuple()

t3 = 10,

print(t1[2])

for valor in t1:
    print(valor)
    
print(t3)

print(t1+t3)

n1,n2,n3,*n,n10=t1
print(n1,n2,n3,*n,n10)