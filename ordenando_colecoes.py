from operator import itemgetter

'''
# Como ordenar coleções através de propriedades
nomes = ['zack', 'camila', 'julios', 'homer']
valores = [2, 34, 55, 76, 78, 89, 78]
nomes.sort()
valores.sort()
# Acima usamos o sort(), mas e abaixo?
# puxe a biblioteca itemgetter de operator, confome acima

pessoas = [{'nome': 'john', 'idade': 32, 'nivel_acesso': 2},
           {'nome': 'carol', 'idade': 18, 'nivel_acesso': 3},
           {'nome': 'tomas', 'idade': 45, 'nivel_acesso': 5},
           {'nome': 'amanda', 'idade': 23, 'nivel_acesso': 1}]

pessoas.sort(key=itemgetter('nome')) # vai ordenar pelo nome
print(pessoas)
# Resposta: [{'nome': 'amanda', 'idade': 23, 'nivel_acesso': 1}, 
# {'nome': 'carol', 'idade': 18, 'nivel_acesso': 3}, 
# {'nome': 'john', 'idade': 32, 'nivel_acesso': 2},
# {'nome': 'tomas', 'idade': 45, 'nivel_acesso': 5}]
# ordenou pelo nome
'''
'''
# CASOS EM LISTA DE TUPLAS
produtos = [('celuar', 750), ('bicicleta', 1500), ('microfone', 550)]
produtos.sort(key=itemgetter(1)) # ordena-se pelo indice, ja que em tuplas não temos chave e valor. O indice 1 neste caso é o preço.
print(produtos)
# Resposta: [('microfone', 550), ('celuar', 750), ('bicicleta', 1500)]

produtos.sort(key=itemgetter(0), reverse=True) # vai ordenar pelo indice 0(letra) em modo inverso
print(produtos)
# resposta [('microfone', 550), ('celuar', 750), ('bicicleta', 1500)]
'''

# CASOS EM MATRIZ DE DADOS
matriz = [[5, 10], [5, 8], [10, 12]]
matriz.sort(key=itemgetter(1))
print(matriz)
# Resposta: [[5, 8], [5, 10], [10, 12]]
