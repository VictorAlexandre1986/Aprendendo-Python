class BaseDeDados:
    def __init__(self):
        self.dados={}
        
    def inserirCliente(self,id,nome):
        if 'clientes' not in self.dados:
            self.dados['clientes']={id:nome}
        else:
            self.dados['clientes'].update({id:nome})

    def excluirCliente(self,id):
        del self.dados['clientes'][id]
    
    #lista clientes        
    def listarClientes(self):
        print('-----------------Clientes-----------------')
        for k,v in self.dados['clientes'].items():
            print(f'chave : {k} , valor : {v}')


bd = BaseDeDados()
bd.inserirCliente(1,'Victor')
bd.inserirCliente(2,'Xispita')
bd.inserirCliente(3,'Nenem')
bd.inserirCliente(4,'Abacaxi')
bd.listarClientes()
bd.excluirCliente(4)
bd.listarClientes()