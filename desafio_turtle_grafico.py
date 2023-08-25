from turtle import Turtle

"""
Perguntar ao usuario sobre a direção
a cada resposta, repetir a pergunta.
"""

t = Turtle()

while True:
    velocidade = int(input('Informe a velocidade: '))
    t.speed(velocidade)
    
    distancia = 0
    direita = 0
    esquerda = 0
    tras = 0
    direção = input('O que quer fazer?:  ')
    
    distancia = int(input('Informe a distância: '))
    t.forward(distancia)
    
    direita = int(input('Informe rotação á direita: '))
    t.right(direita)
    
    esquerda = int(input('Informe rotação á esquerda: '))
    t.left(esquerda)
    
    #c = int(input('Informe quantos píxels para cima: '))
    #t.up()
    
    #b = int(input('Informe quantos píxels para baixo: '))
    #t.down()
    
    traz = int(input('Informe quantos pixels para tras: '))
    t.backward(traz)
    
    input()