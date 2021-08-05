import threading
import time

def main():
    
    threads = [
        threading.Thread(target=contar, args=('elefante',10)),
        threading.Thread(target=contar, args=('gato',8)),
        threading.Thread(target=contar, args=('pato',20)),
        threading.Thread(target=contar, args=('cachorro',15)),
    ]
    [th.start() for th in threads]
    
    print('\nPodemos fazer outras coisas no programa enquanto a thread vai executando...')
     
    [th.join() for th in threads]
    
    print('Pronto!!!')
    
    

def contar(animal,numero):
    for n in range(1,numero+1):
        print(f'{n} {animal}(s)...')
        time.sleep(1)
        

if __name__=='__main__':
    main()
