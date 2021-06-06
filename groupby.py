from itertools import groupby,tee

alunos=[
    {'nome':'Victor','nota':'A'},
    {'nome':'Alexandre','nota':'B'},
    {'nome':'Braga','nota':'C'},
    {'nome':'Ribeiro','nota':'D'},
    {'nome':'Xandinho','nota':'A'},
    {'nome':'Fifi','nota':'A'},
    {'nome':'Xispita','nota':'B'},
    {'nome':'Nenem','nota':'C'},
    {'nome':'Peta','nota':'B'},
    {'nome':'Banca','nota':'B'},
    {'nome':'Ximbica','nota':'A'},
    {'nome':'Xaquira','nota':'A'},
    {'nome':'Sherek','nota':'C'},
    {'nome':'Peto','nota':'C'},
]
ordena = lambda aluno:aluno['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento,valores_agrupados in alunos_agrupados:
    
    va1,va2 = tee(valores_agrupados)
    print(f'Agrupamento : {agrupamento}')
    print(f'{len(list(va1))} alunos tiraram a nota {agrupamento}')
    
    for aluno in va2:
        print(aluno)
    print()