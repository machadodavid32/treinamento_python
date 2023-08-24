"""

# Continue > ignorar, pular
for numero in range(100):
    if numero % 2 == 0:  # se o número for par
        print(numero)
    else:
        continue
    

# break, interrompe a operação
        
for numero in range(100):
    if numero % 2 == 0:  # se o número for par
        print(numero)
    else:
        break


frutas = ['maça', 'manga', 'laranja', 'morango']
for fruta in frutas:
    if fruta == 'manga':
        continue # o continue vai ignorar a manga
    print(f'{fruta} adicionada a dieta')    
# maça adicionada a dieta
#laranja adicionada a dieta
#morango adicionada a dieta 
           
frutas = ['maça', 'manga', 'laranja', 'morango']
for fruta in frutas:
    if fruta == 'manga':
        break # o break vai parar o programa quando chegar em manga, vai imprimir somente maça  
    print(f'{fruta} adicionada a dieta')           
"""

estilos = ['hip-hope','rock','rap','pop']
for estilo in estilos:
    if estilo == 'rap':
        continue
    print(f'{estilo} tocando')
        
estilos = ['hip-hope','rock','rap','pop']
for estilo in estilos:
    if estilo == 'rock':
        break
    print(f'{estilo} tocando')
             