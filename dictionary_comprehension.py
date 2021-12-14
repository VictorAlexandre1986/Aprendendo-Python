dicionario={'a':1, 'b':2, 'c':3, 'd':4}

quadrado = {chave: valor**2 for chave,valor in dicionario.items()}

print(quadrado)




chaves='abcde'
valores=[1,2,3,4,5]

mistura = {chaves[i]:valores[i] for i in range(1,len(chaves))}
print(mistura)





res = {num:('par' if num%2==0 else 'impar')for num in range(1,10)}
print(res)