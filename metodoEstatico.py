import random

class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        
    @staticmethod
    def gera_id():
        rand = random.randint(1,1000)
        return rand
    
#Tando a classe quanto o objeto pode invocar o método
p1 = Pessoa('Victor',35)
print(p1.gera_id())
print(Pessoa.gera_id())