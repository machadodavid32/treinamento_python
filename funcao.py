from datetime import datetime

def dar_boas_vindas(nome):
    print(f'ola {nome}')
    
    
dar_boas_vindas('David')    


def informacao_padrao(lugar='nossa loja'):
    print(f'Conheça nossa `{lugar}')
    
informacao_padrao()    # informação padrão já definida 'nossa loja'
informacao_padrao('minha loja') # porém pode ser modificada

# Todo argumento com valor padrão deve ser passado no final caso haja mais de um argumento

def criar_nome_completo(nome, sobrenome):
    print(f'Seu nome é {nome} {sobrenome}')
    

criar_nome_completo('David', 'Machado')    

def calculo(quantidade, preco=1):
    print (quantidade * preco)

calculo(4, 8.90)


def gerar_objeto_personalizado(cor,*, altura,formato): # após o *, todos os argumentos terão que ser nomeados, conforme...
    # .. a chamada da função abaixo
    print(cor, altura, formato)
    
gerar_objeto_personalizado('branco', altura=1.75, formato='fisico')    


def somar(*valores, b):  #O * serve para que se coloque varios valores no argumento  > *args
    print(valores)
    for valor in valores:
        b += valor
    print(b)
    
somar(10, 20, 5, b=5)
# Resposta: 40        


def contatenar(**palavras):  # Aqui se chama **kwargs, que da pra passar varios argumentos
    frase = ''   # só pra criar uma variável que usaremos mais abaixo
    for palavra in palavras.values():
        frase += palavra + ' '  # quando usamos o += quer dizer que estamos adicionando algo para o restante. frase+palavras adiconadas
    print(frase)

contatenar(a='nós', b='somos', c='pythonistas')
        
        
# *args = quantidade ilimitada ARGUMENTOS POSICIONAIS
# **kwargs = quantidade limitada de argumentos NOMEADOS         


def pai(numero):
    def filho_1():
        print('sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1  # reparar que coloquei a função mas não a chamei. Ela será usada posteriormente.
    
resultado = pai(1)
resultado()
# resposta: sou filho 1    >>> Agora a função filho_1 foi usada.


def meu_decorator(funcao):
    def wraper():
        print('antes')
        funcao() # abaixo, vamos criar uma função e, ao chamar esta função, colocaremos a outra pra combinar as duas.
        print('depois')
    return wraper

def parabenizar():
    print('Parabens')
    

resultado_a = meu_decorator(parabenizar)  # Combinei as duas funções.
resultado_a()        

# antes
#Parabens
#depois                       
                    
# A FORMA MAIS COMUM DE USAR UM DECORATOR                    
def meu_decorator(funcao):
    def wraper():
        print('antes')
        funcao() # abaixo, vamos criar uma função e, ao chamar esta função, colocaremos a outra pra combinar as duas.
        print('depois')
    return wraper

@meu_decorator
def parabenizar():
    print('Parabens')


parabenizar()
# Resposta: antes
# Parabens
# depois


def horario_atual(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor

@horario_atual
def baixar_musicas():
    print('baixando musicas')

baixar_musicas()            

# 2023-08-18 19:58:00.723310
# baixando musicas
# 2023-08-18 19:58:00.723310    


# Explicação da função acima
# primeira linha = criar a função com um argumento chamado 'funcao'
# segunda lina = criar uma funcao interna sem argumento, que vai imprimir a hora atual...
# ....vai chamar outra funcao e vai imprimir o horario atual novamente.
# usar a funcao 'horario_atual()' como decorator
# criar a função chamada 'baixar_musicas()' com a função de printar uma frase 'baixando musicas'

# executar a função baixar_musica com decorator da função horario_atual
# assim, ao chamar a função, as duas funções serão combinadas, e a função baixar_musicas() será executada..
# junto com  a função horario_atual()