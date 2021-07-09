class BaseDeDados:
    def __init__(self):
        self.__dados={}
    
    
    @property
    def dados(self):
        return self.__dados
    
    
    @dados.setter
    def dados(self,id,valor):
        self.dados['clientes'].update({id:valor})
            
            
    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({ id:nome })
            
            
    def lista_clientes(self):
        for chave,valor in self.__dados['clientes'].items():
            print(chave,valor)
    
    
    def apagar_clientes(self,id):
        return self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1,'Victor')
bd.inserir_cliente(2,'Xispita')
bd.inserir_cliente(3,'Nenem')
bd.inserir_cliente(4,'Fifi')
bd.lista_clientes() 
