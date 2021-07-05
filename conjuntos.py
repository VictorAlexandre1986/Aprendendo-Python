lista = [1,1,1,2,34,5,6,7,8,7,8,5,6,5,4,2]

#Sets não aceita elementos duplicados
s1 = set(lista)
print(s1)

#Adiciona 
s1.add(50)
print(s1)

#Remove
s1.discard(34)
print(s1)

#INSERE SOMENTE ITERAVEL
s1.update('Python')
print(s1)

s2={1,2,3,4,5,7}
s3={1,2,3,4,5,6,8,9}

#Uniao dos sets
print(f'União : {s2 |s3}')

#Está presente nos dois sets
print(f'Intersecção : {s2 & s3}')

#Elementos que estão somente no set da esquerda
print(f'Diferença : {s2 - s3}')

#Elementos que estão nos dois sets, mas não em ambos
print(f'Diferença simetrica : {s2 ^ s3}')


