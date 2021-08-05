import time

from threading import Thread
from queue import Queue

def gerador_de_dados(queue):
    for i in range(1,11):
        print(f'Dados {i} gerado.')
        time.sleep(2)
        queue.put(i)
        
def consumidor_de_dados(queue):
    while queue.qsize()>0:
        valor = queue.get()
        print(f'dados {valor*2} processado.')
        time.sleep(1)
        queue.task_done()
        
if __name__=='__main__':
    queue = Queue()
    th1 = Thread(target=gerador_de_dados, args=(queue,))
    th2 = Thread(target=consumidor_de_dados, args=(queue,))
    
    th1.start()
    th1.join()
    
    th2.start()
    th2.join()
    
    
    
                 
                 