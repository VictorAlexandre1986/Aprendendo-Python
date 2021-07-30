#Ao escrever uma função que receba um parametro nutavel, voce deve considerar 
# cuidadosamente se quem chama espera que o argumento passado seja alterado.

#Uma classe que mostra os perigos de alterar argumentos recebidos

class TwilightBus:
    '''Um modelo de onibus que faz os passageiros desaparecerem'''
    
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            #nessa atrbuição faz self.passengers ser um apelido para passengers
            self.passengers=passengers
    
    #Os métodos abaixo estão alterando o método original
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)
        


class TwilightBusCorrigidos:
    #Agora o argumento passado para o parametro passenger  pode ser qualquer iterável
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            #Faz uma cópia da lista passengers ou converte para uma list,se ele não for lista
            self.passengers=list(passengers)
    
    def pick(self,name):
        self.passengers.append(name)
        
    def drop(self,name):
        self.passengers.remove(name)