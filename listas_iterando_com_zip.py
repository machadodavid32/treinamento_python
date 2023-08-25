from itertools import zip_longest # serve para iterar com multiplas listas, mesmo que uma tenha menos iténs que outras

a_lista = ['A','B','C','D','E']
b_lista = [1, 2, 3, 4, 5, 6]

for a, b in zip(a_lista, b_lista):
    print(a)
    print(b)
#resposta> A1B2C3.....

produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250, 150, 220, 550, 20]

for a, b in zip(produtos, precos):
    print(f'Salvando produto {a} valor R${b}')
# Resposta: 
# Salvando produto produto 1 valor R$250
# Salvando produto produto 2 valor R$150
# Salvando produto produto 3 valor R$220
# Salvando produto produto 4 valor R$550
# Salvando produto produto 5 valor R$20         


titulos = ['titulos 1', 'titulos 2', 'titulos 3', 'titulos 4',]
descricoes = ['descricao 1', 'descricao 2', 'descricao 3']

for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo}, descrição {descricao}')

# Resposta:
# Encontramos o titulos 1, descrição descricao 1
# Encontramos o titulos 2, descrição descricao 2
# Encontramos o titulos 3, descrição descricao 3
# Encontramos o titulos 4, descrição None    


    