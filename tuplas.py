# Tuplas não podem ser alteradas

sites = ('youtube.com', 'facebook.com','instagram.com')
valores = (23, 45, 65)

# acessando items
print(sites[1])
# Resposta: facebook.com
print(valores[2])
# Resposta: 65

# União de tuplas
dados_sistema = sites + valores
print(dados_sistema)
# Resposta: ('youtube.com', 'facebook.com', 'instagram.com', 23, 45, 65)

