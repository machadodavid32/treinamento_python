"""
Como criar e modificar arquivos no Python
'r' -> Usado somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo

"""

import os

with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Aqui se escreve o conteúdo')