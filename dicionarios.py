# um dicionario
dicionario_pessoa = {'nome': 'Carol', 'Idade': 18, 'altura': 1.65}
print(dicionario_pessoa)

# um outra forma de fazer um dicionário
dicionario_pessoa2 = dict(nome='Carol', idade=18, altura=1.65)
print(dicionario_pessoa2)


# acessando um valor especifico - sempre pega chave
#print(dicionario_pessoa2['idade'])
# resposta: 18

# Acessando todas as chaves disponiveis
#print(dicionario_pessoa.keys())
# resposta: dict_keys(['nome', 'Idade', 'altura'])

# Acessando todos os valores dentro das chaves
#print(dicionario_pessoa.values())
# resposta: dict_values(['Carol', 18, 1.65])

# Acessando todos as chaves e valores
#print(dicionario_pessoa.items())
# Resposta: dict_items([('nome', 'Carol'), ('Idade', 18), ('altura', 1.65)])

# Iterar sobre um dicionario
for item in dicionario_pessoa2.items():
    print(item[1])

# resposta: 
# Carol
#18
#1.65    


