# métodos de uma classe, ligar, desligar, exibir dados do computador(classe usada como exemplo)

class Computador:
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
    

computador1 = Computador('Asus', '32gb', 'Nvidia')
computador1.ligar()
computador1.desligar()
computador1.exibir_dados_do_computador()        
