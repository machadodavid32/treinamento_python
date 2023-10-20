from array import array

# São três tipos de arrays: valores inteiros, numeros inteiros decimais e caracteres

# https://docs.python.org/pt-br/3.7/library/array.html

numeros = array('i', [1,2,3,4,5,6]) # O 'i' quer dizer numeros inteiros - retirado da documentação acima.
numeros.app(10) # Adicionando valor a lista
numeros.insert(5, 200) # adicionando o valor 200 na posição 5
numeros.pop(1) # extraindo o numero 1 da lista
numeros.remove(5) # removendo o valor 5 da lista
del numeros[1] # removendo o indice 1, lembrando que podemos remover uma faixa de indices - [1:3] por exemplo



