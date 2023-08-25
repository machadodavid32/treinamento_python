valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2020]

# Adicionar ao final da lista
valores.append(11)
print(valores)

# Adicionar em qualquer lugar na lista
anos.insert(2, 2031) # indice e item
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2020, 2030, 2031, 2040, 2020]

# unir listas
valores.extend(anos) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2020, 2030, 2040, 2020] 
print(valores)


# extrair com base no indice
anos.pop(4)
print(anos)

# extrair com remove - pelo item
anos.remove(2030)
print(anos)

# extrair pelo indice usando del, que elimina varios se quiser
del anos[2] # [2020, 2031, 2040]

del valores[2:5] # começa em dois e termina no 5
print(valores)
# [1, 2, 6, 7, 8, 9, 10, 11, 2020, 2030, 2031, 2040, 2020]

# Contando ocorrências dentro de uma lista
print(valores.count(2)) # quantas vezes o numero dois aparece na lista

# Apagando todos os iténs de uma lista
valores.clear()
print(valores) # [] > lista zerada

