"""Métodos mágicos é, por exemplo, o __init__ que tem certas funções que não aparecem no código.
Existem outros como __new__ que tem outra funcionalidade"""

class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma pessoa'
        

pessoa = Pessoa()
print(pessoa.nome)
# Resposta: Sou uma pessoa            

import datetime  # Aperte f12 aqui pra ver o código da função

