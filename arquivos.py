# This is a sample Python script.
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

caminho='C:\\'
def verifica(caminho):
    # Verifica as pastas e arquivos dentro da pasta
    print(f'Hi, {os.listdir(caminho)}')  # Press Ctrl+F8 to toggle the breakpoint.
    #outra maneira é usando o abspath
    print(os.path.abspath('.')) #Verificando o caminho do diretorio atual
    print(os.path.abspath('venv'))

    #Criando caminho
    print(os.path.join('C:\\','Arquivos de programas'))

def comandos_so():
    #Permite inserir comandos do sistema operacional
    os.system('dir')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verifica(caminho)
    comandos_so()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
