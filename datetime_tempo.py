from datetime import datetime

print(datetime.now()) # mostra data e hora atual
print(datetime.now().day) # mostra o dia
print(datetime.now().month) # o mes
print(datetime.now().year) # o ano
print(datetime.now().hour) # a hora


# CRIAR UMA DATA    
lancamento_app = datetime(2025, 12, 8)
print(lancamento_app)  # resposta: 2025-12-08 00:00:00

# PEDINDO UMA DATA AO USUARIO E CONVERTENDO EM DATETIME E FORMA DO BRASIL

data_lancamento = datetime.strptime(input('Informe a data de lançamento: '), '%d/m%/y%')
print(data_lancamento.strftime("%d/%m/%Y"))
print(type(data_lancamento))
