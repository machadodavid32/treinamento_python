"""
Como criar e modificar arquivos no Python
'r' -> Usado somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo

"""

import os

# Criando um arquivo
with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Aqui se escreve o conteúdo')

# Criando um arquivo com poder de adicionar dados usando 'a'
nomes = ['lucas','carol', 'jeff', 'doulgas']
numeros = [1, 2, 3, 4, 5, 6]

with open('numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)  # Estou criando um arquivo com separação de linhas 
           
# lendo um arquivo
with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
        

# Lendo um arquivo e adicionando dados
with open('numeros.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.write('9000')                
    

    