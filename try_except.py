# Evitando que seu programa trava
try:
    valor = int(input("Digite um valor em dolar: "))
    print( valor * 5.90)
except:
    print("Favor digitar apenas números")    