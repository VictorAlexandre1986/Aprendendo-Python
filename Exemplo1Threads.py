import threading
import time

def main():
    th = threading.Thread(target=contar, args=('elefante',10))
    
    th.start()
    
    print('\nPodemos fazer outras coisas no programa enquanto a thread vai executando...')
    
    th.join()
    
    print('Pronto!!!')
    
    

def contar(animal,numero):
    for n in range(1,numero+1):
        print(f'{n} {animal}(s)...')
        time.sleep(1)
        

if __name__=='__main__':
    main()
