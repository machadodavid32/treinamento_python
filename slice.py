teclado = 'teclado'

print(teclado[2])

print(teclado.index('l'))

nome = 'David de Araujo Machado'
print(nome[0:5]) # iniciando do caracter 0 até 4 (não conta o quinto)
print(nome[2:]) # via imprimir o indices a partir do indice 3

pegando_indice = nome.rindex("D")
pegando_indice_final = nome.rindex("o")

print(nome[pegando_indice:pegando_indice_final+1])
# resposta: David de Araujo Machado
