#Um decorador é um invocável que aceita outra função como argumento(a função decorada)
#O decorador pode realizar algum processamento com a função decorada e devolvê-la
# ou substituila por outra função ou um objeto incocavel.


    
def deco(funcao):
    def inner():
        print('running inner()')
    
    return inner

@deco
def vaiChamarAOutraFuncao():
    print('running targer()')
    
vaiChamarAOutraFuncao()

#Uma caracteristica fundamental dos decoradores é que eles são executados imediatamente
#apos a funcao decorada ser definida

#registry armazenará referencias as funções decoradas com @register
registry = []
#register recebe uma função como argumento
def register(func):
    #exibindo a função que está sendo decorada
    print('running register(%s)' % func)
    #incluindo a função no registry
    registry.append(func)
    return func

#Decorada com register
@register
def f1():
    print('running f1()')
    
@register
def f2():
    print('running f2()')
    
#não é decorada
def f3():
    print('running f3()')

#main exibe registry e então chama f1(), f2() e f3()
def main():
    print('running main()')
    print('registry ->, ', registry)
    f1()
    f2()
    f3()
#observe que register executa duas vezes antes de qualquer outra função 
#Depois que o módulo é carregado,registry contém referencias para as duas funções decoradas
#Essas funções ,assim como f3, são executadas somente quando chamdas explicitamente por main



if __name__=='__main__':
    main()