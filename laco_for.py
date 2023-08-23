"""
for numero in range(5): # vai do 0 até 4
    print('carregando', numero)


for numero in range(1, 6): # vai do 1 até 5
    print('carregando', numero)
    
for numero in range(1,10, 2): # vai do 1 até 10 contando de 2 em 2
    print('carregando', numero)    
    

nomes = ['Arthur', 'Aline', 'David']
for nome in nomes:
    print(nome)


for numero in range (18, 111):
    print(numero)
"""    
celulares = ['asus', 'samsung', 'sony', 'iphone', 'xiaomi', 'motorola']
versoes = ['plus','premium','premium plus','plus deluxe','ultra plus']

for celular in celulares:
    for versao in versoes:
        print(f' {celular} {versao}')