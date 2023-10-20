# Criar ou ler aquivos json existente usando python

import json

computador_json = """
{
    "marca": "Dell",
    "preço": 15000
}
"""
# Lendo um string JSON
data = json.loads(computador_json) # transforma strings para dicionário
print(data["preço"])
# 15000

# Salve um string JSON em um arquivo JSON
with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json) # criando o arquivo
    # Criado arquivo computador.json
    

# Para ler um arquivo JSON
with open('computador.json', encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # convertendo json para string
    dicionario_computador_json = json.loads(string_computador_json) # converter de string para dicionário python
    print(dicionario_computador_json["marca"]) 


    
        
# Abaixo,desafio json

desafio_json = """
{
    "name": "John Smith",
    "Age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}

"""

d_json = json.loads(desafio_json) # transforma strings para dicionário

with open('d.json', 'w', encoding='utf-8') as arquvivo_djson:
    json.dump(d_json, arquvivo_djson) # Criando arquivo
    

