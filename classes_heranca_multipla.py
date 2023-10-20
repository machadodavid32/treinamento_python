"""Herança multipla nos permite unir métodos e funções de varias classes em uma só"""

class Pessoa():
    nome = 'Sou uma pessoa'


class Profissional():
    nome = 'Sou um profissional'
    

class AtorProfissional(Pessoa, Profissional):
    pass

        
    

