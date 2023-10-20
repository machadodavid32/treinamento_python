'''
idade = input("Digite a sua idade: ")

# print(idade > 17)
# Vai dar o seguinte erro: TypeError: '>' not supported between instances of 'str' and 'int'

# Então resolvemos desta forma
#print(int(idade) > 17) # transformei idade em numero inteiro


# outro caso abaixo
ano_publicacao = 2020
#print('Este livro foi criado em' + ano_publicacao)
# vai dar este erro: TypeError: can only concatenate str (not "int") to str

# Mas ai podemos resolver deste modo:
print('Este livro foi criado em ' + str(ano_publicacao))

'''

# Conversões entre coleções
saudacao = 'Hello!'
print(list(saudacao)) # ['H', 'e', 'l', 'l', 'o', '!']
print(set(saudacao)) # {'o', 'e', '!', 'H', 'l'}
print(tuple(saudacao)) # ('H', 'e', 'l', 'l', 'o', '!')