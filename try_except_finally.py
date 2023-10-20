internet = None

try:
    print('Fazendo conexão com a ' + internet) # Aqui vai dar erro TypeError no terminal.(string + boleano não da match)
except TypeError as erro:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra')     