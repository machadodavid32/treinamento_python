import random

print(random.random()) # imprime valores aleatorios de 0.0 a 1.0

print(random.uniform(4, 10)) # Roda valores aleatórios de 4 até 10

print(random.randint(4, 10)) # gera valores aleatórios inteiros de 4 até 10

cores = ['verde', 'vermelho', 'azul']
print(random.choice(cores))  # vai escolher um dos elementos da lista acima


print(random.choices(cores, k=2)) # vai escolher dois elementos da lista acima


cartas_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
print(random.shuffle(cartas_baralho)) # Vai embaralhar a lista acima.
print(cartas_baralho) # tem que dar outro print

cara_coroa = ['cara','coroa']
print(random.choice(cara_coroa))

nomes = ['Aline', 'Arthur', 'Guilherme', 'David', 'Danilo']
print(random.choice(nomes))

print(random.randint(10, 100))



