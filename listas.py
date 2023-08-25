preco = [10, 20, 30, 48, 50, 60, 70, 100, 110]

# Encontrando um itém pelo valor do item
print(preco[preco.index(100)])

itens = [1, 3, 6, 'ola', 'tudo bem', True, 10.6]
print(itens[4]) # Acessando index 4 > 'tudo bem'

# MODO DE CRIAÇÃO DE LISTAS

lista_de_noves = [9] * 11
print(lista_de_noves) # resposta> [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]

lista_usando_range = list(range(20)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(lista_usando_range)

lista_de_caracteres = list('Bem vindo David')
print(lista_de_caracteres) # ['B', 'e', 'm', ' ', 'v', 'i', 'n', 'd', 'o', ' ', 'D', 'a', 'v', 'i', 'd']    

# LISTA DE LISTA(MATRIZ)
matriz_de_nomes = [['Carol', 30], ['Marcus', 45]]
print(matriz_de_nomes[0]) # ['Carol', 30]
print(matriz_de_nomes[0][0]) # Carol  Aqui se acessa o itém da lista dentro da lista.


objetos = ['computador', 'cadeira', 'celular']
print(objetos)

desafio2 = list(range(10, 132))
print(desafio2)

desafio3 = objetos + desafio2
print(desafio3)

desafio4 = [['computador', 2600], ['cadeira', 400], ['celular', 600]]
print(desafio4)

