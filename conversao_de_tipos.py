# Conversão de tipos

idade = input('Qual a sua idade?') # vai gerar uma string
print(int(idade) > 18)  # vai ser convertido para o tipo int

# convertendo int para string
print(type(str(5)))  # > somente str(5)
# <class 'str'>

altura_parede = input('Qual é a altura da parede?')
print(float(altura_parede) > 2.10)


# Existem também conversões para list(), tuple() e dict()