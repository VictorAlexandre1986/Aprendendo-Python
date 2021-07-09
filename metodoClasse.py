class Pessoa:
    ano_atual = 2021
    
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        
    def get_ano_nasc(self):
        print(self.ano_atual - self.idade)
        
    @classmethod
    def get_idade(cls,nome,ano_nasc):
        idade = Pessoa.ano_atual-ano_nasc
        return cls(nome,idade)        

p1 = Pessoa('Victor',35)
p1.get_ano_nasc()

p2=Pessoa.get_idade('Victor',1986)
p2.get_ano_nasc()


    