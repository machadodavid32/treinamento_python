# Tipos de variaveis em uma classe

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
    
    def exibir_dados_do_computador(self):  # self permite acesso as propriedades que estão dentro do construtor __init__ (marca, memoria ram, placa de video)            
        print(f'Computador da marca {self.marca},com {self.memoria_ram} de memoria ram e que usa a placa de video {self.placa_de_video}')
    

computador = Computador('Asus', '32gb', 'nvidia')
print(computador.marca)
print(computador.sistema_operacional)
# Asus -> Aqui vc precisou colocar a marca
# Windows 10 -> reparar aqui que vc não precisou colocar qual sistema, pois ja está como padrão

# porém, da pra mudar o valor da variavel de classe
Computador.sistema_operacional = 'Linux'

print(computador.sistema_operacional)

