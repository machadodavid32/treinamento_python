# Métodos de classe (Class methods) e estatisticos (Static Methods)

class Computador:
    sistema_operacional = 'Windows 10' # variavel de classe, será sempre inclusa com as outras variaveis como padrão.
    # Variavel da classe pode ganhar novos valores
    
    
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    def ligar(self):
        print('Estou ligando o computador')
    
    def desligar(self):
        print('Desligando o computador')
    
    def exibir_dados_do_computador(self):  # exibir_dados_do_computador é um método comum,..
        # ele acessa as propriedade da instancia através do self            
        print(f'Computador da marca {self.marca},com {self.memoria_ram} de memoria ram e que usa a placa de video {self.placa_de_video}')
        

 # Class methods - Usada para modificar como uma classe é instanciada
 
 # Vamos imaginar que temos uma loja que monta computadores, e temos config padrão para cada tipo de cliente:
 
 # Configuração para cliente de escritório
 # Configuração para clientes de trabalho pesado(jogos, videos, 3d)
    @classmethod
    def computador_escritorio(cls, memoria_ram): # cls quer dizer que estamos passando a classe inteira como parâmetro, não a instancia
         return cls('Dell', memoria_ram, 'Placa de Video - Baixo custo')
    
    @classmethod
    def computador_configuracao_pesado(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video - Alto nivel') 
    
    
    # Statich methods - Não usam a instancia da classe através do self e não mudam as propriedades da classe através do cls
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            False


# Computador roda programa pesado?
print(Computador.roda_programas_pesados(10)) # dez gigas    

# Computador escritório    
computador1 = Computador.computador_escritorio('8gb')


# computador para jogos
computador2 = Computador.computador_configuracao_pesado('32GB')

computador1.exibir_dados_do_computador()

print('##########')

computador2.exibir_dados_do_computador()

# RESPOSTA
# Computador da marca Dell,com 8gb de memoria ram e que usa a placa de video Placa de Video - Baixo custo
##########
# Computador da marca Dell,com 32GB de memoria ram e que usa a placa de video Placa de Video - Alto nivel






 