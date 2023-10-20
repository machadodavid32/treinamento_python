from turtle import Turtle

"""
Perguntar ao usuario sobre a direção
a cada resposta, repetir a pergunta.
"""

t = Turtle()

velocidade = int(input('Informe a velocidade: '))
t.speed(velocidade)

while True:
    
    
    distancia = 0
    direita = 0
    esquerda = 0
    tras = 0
    direcao = input('O que quer fazer?: di = distancia, d = rotação a direita, e = rotacao a esquerda, t = ir para tras ')
    
    if direcao == 'di':
        distancia = int(input('Informe a distância: '))
        t.forward(distancia)
    
    elif direcao == 'd':    
        direita = int(input('Informe rotação á direita: '))
        t.right(direita)
    
    elif direcao == 'e':
        esquerda = int(input('Informe rotação á esquerda: '))
        t.left(esquerda)
    
    elif direcao == 't':
        tras = int(input('Informe quantos pixels para tras: '))
        t.backward(tras)    
    else:
        print('Até mais')
        break
    
    
    
    
    
    #c = int(input('Informe quantos píxels para cima: '))
    #t.up()
    
    #b = int(input('Informe quantos píxels para baixo: '))
    #t.down()
    
    