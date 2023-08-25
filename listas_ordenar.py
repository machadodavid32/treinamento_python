valores = [15, 12, 45, 33, 1 , 20, 4, 6, 100, 102]

valores.sort()
print(valores) # [1, 4, 6, 12, 15, 20, 33, 45, 100, 102]

valores.sort(reverse=True) # ordem inversa
print(valores) # [102, 100, 45, 33, 20, 15, 12, 6, 4, 1]

valores.reverse() # Aqui ele inverte a lista sem ordenar
print(valores) # [102, 100, 6, 4, 20, 1, 33, 45, 12, 15]

