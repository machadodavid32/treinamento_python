# Como podemos criar listas?

# Criando usando loops com range
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)    

# Criando listas com map
nomes = ['Larissa','Rafael','Marcos','Jonas']
def aprovar_pessoa(nome):  # Aqui a possibilidade de aplicar uma função para fazer efeito dentro de uma lista!
    return nome +' APROVADO'

print(list(map(aprovar_pessoa, nomes)))
# ['Larissa APROVADO', 'Rafael APROVADO', 'Marcos APROVADO', 'Jonas APROVADO']


 

