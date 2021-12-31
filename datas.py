import datetime

#Pegando a data atual
print(f'Data atual : {datetime.datetime.now()}')

#alterar o valor dos campos
inicio = datetime.datetime.now()
inicio = inicio.replace(year=2021, month=8, day=1, hour=16, minute=30, second=0, microsecond=0)
print(f'Data alterada : {inicio}')

#criando um data
evento=datetime.datetime(year=2022, month=5, day=29)


#Convertendo string em datetime
nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
nascimento=nascimento.split("/")
nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))
print(f'Data de nascimento : {nascimento}')

#Convertendo string para datetime segunda forma
nascimento = input("Qual sua data de nascimento ? (dd/mm/yyyy) :")
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)

#Acessando os elementos individualmente
evento = datetime.datetime.now()

print(f'dia = {evento.day}')
print(f'mes = {evento.month}')
print(f'ano = {evento.year}')
print(f'hora = {evento.hour}')
print(f'minuto = {evento.minute}')
print(f'segundos = {evento.second}')


#trabalhando com diferença de datas
data_hoje = datetime.datetime.now()
aniversario= datetime.datetime(year=1986, month=5, day=29)
data_evento = data_hoje - aniversario
print(data_evento)
print(f'Faltam {data_evento.days} dias, {data_evento.seconds // 3600} horas')

#boleto criando um data de vencimento
data_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=5)
vencimento_coleto = data_compra + regra_boleto
print(f'Data da compra : {data_compra}')
print(f'Data do vencimento : {vencimento_coleto}')

#Mudança ocorrendo meia noite
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

#Encontrar os dias da semana

#0 - Segunda-feira
#1 - Terça-feira
#2 - Quarta-feira
#3 - Quinta-feira
#4 - Sexta-feira
#5 - Sabado
#6 - Domingo

print(manutencao.weekday())

#Acha o dia da semana que nasceu
aniversario = input("Qual sua data de nascimento ? (dd/mm/yyyy)")
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
if aniversario.weekday()==0:
    print('nasceu na segunda-feira')
elif aniversario.weekday()==1:
    print('nasceu na terça-feira')
elif aniversario.weekday()==2:
    print('nasceu na quarta-feira')
elif aniversario.weekday()==3:
    print('nasceu na quinta-feira')
elif aniversario.weekday()==4:
    print('nasceu na sexta-feira')
elif aniversario.weekday()==5:
    print('nasceu no sábado')
else:
    print('nasceu no domingo')


#formatando data e hora
hoje = datetime.datetime.now()

hoje_formatado = hoje.strftime('%d/%m/%Y - %H:%M:%S')

print(hoje_formatado)

def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    if data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    if data.month == 3:
        return f'{data.day} de Março de {data.year}'
    if data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    if data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    if data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    if data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    if data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    if data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    if data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    if data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    if data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


mes=formata_data(hoje)
print(mes)

#Formatando dado de outra maneira
#pip install TextBlob
#def formata_data1(data):
#    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

#trabalhando com hora
hora=datetime.time(12,12,12)
print(hora)

#Pegando o timestamp
data = datetime.datetime.now()
#convertendo a data para timestamp
data = data.timestamp()
#convertendo timestamp para data
data = datetime.fromtimestamp(data)


#Traduzindo datas
from locale import setlocale,LC_ALL

setlocale(LC_ALL,'pt_BR.utf-8')

dt = datetime.datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)

#Saber quantos dias tem o mês
from calendar import mdays

dt = datetime.datetime.now()
mes_atual = int(dt.strftime('%m'))
print(mes_atual, mdays[mes_atual])