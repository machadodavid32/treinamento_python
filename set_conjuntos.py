# Não repetem valores
numeros = [2, 2, 5, 8]
frutas = {'maça', 'uva', 'banana', 'maça', 'morango'}

#set_numeros = set(numeros)
#print(set_numeros)
# {8, 2, 5}

#set_frutas = set(frutas)
#print(set_frutas)
# {'morango', 'banana', 'uva', 'maça'}


# da pra adicionar
#set_numeros.add(10)
#print(set_numeros)
# {8, 2, 10, 5}


numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)

print(a.symmetric_difference(b)) # diferenças entre um e outro, valores que estão presente em um, mas não no outro.
# resposta: {3, 5, 8, 9}

print(a.intersection(b)) # intersecção entre os dois - numeros em commum entre os dois sets
# {2}

print(a.union(b)) # União dos dois sets
# {2, 3, 5, 8, 9}