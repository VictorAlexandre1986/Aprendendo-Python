import logging

#Niveis de mensagem
#INFO
#DEBUG
#WARNING
#ERROR
#CRITICAL

formatar = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename="log.log", encoding='utf-8' ,level=logging.DEBUG,format=formatar,datefmt="%d/%m/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)
#ou
#logger = logging.getLogger(__file__) Mostras o arquivo e seu caminho

class Calculadora:
    def __init__(self, *args, **kwargs):
        logger.info("Começou...")
        
    def gravar(self):
        with open('arquivo.txt','a') as arquivo:
            arquivo.write('Gravando...')
        logger.info('Dentro do método gravar')

    def somar(self,n1,n2):
        return(n1+n2)
    
    
    def divisao(self,n1,n2):
        return(n1/n2)

        
        
if __name__ == '__main__':
    calc = Calculadora()
    calc.gravar()
    try:
        calc.divisao(10/0)
    except (ZeroDivisionError) as e:
        #logger.error('Não é possível dividir por zero!!!')
        logger.exception('Error : ')