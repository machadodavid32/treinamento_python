nomes = ['Larissa','Rafael','Marcos','Jonas']

def pessoa_aprovada(pessoa):
    if pessoa == 'Marcos':
        return True
    else:
        return False
    

print(list(filter(pessoa_aprovada, nomes)))    
# Resposta: ['Marcos']


# para processar todos os dados, usa-se o map, para especifico de um dado, usa-se filter

pinturas = [['pintura classica', 'azul', 1857],
            ['pintura medieval', 'vermelha', 1867],
            ['pintura moderna', 'verde', 1897]]

def antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False
    
print(list(filter(antiguidade, pinturas)))

# Resposta: [['pintura classica', 'azul', 1857], ['pintura medieval', 'vermelha', 1867]]
  
  
vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
    ]    

def salario(vag):
    if vag[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(salario, vagas)))
# [['vaga 2', 2550], ['vaga 3', 5000]]

    
    