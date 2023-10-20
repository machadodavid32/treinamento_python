# Enumerate - Saiba qual é o indice que estamos iterando no momento

for indice, numero in enumerate(range(1, 11), 1): # Aqui ele vai enumerar os indices a partir do 1, mas pode ser por outro indice, 2, 3,...
    print(indice, numero)
#1 1 indice e valor
#2 2
#3 3
#4 4
#5 5
#6 6
#7 7
#8 8
#9 9
#10 10

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']
for indice, nome in enumerate(nomes, 1):
    print(indice, nome)
    if indice == 3:
        print(f'chegamos ao indice {indice}')
        
