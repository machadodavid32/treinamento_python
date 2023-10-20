#classes

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video


# instancias - São as variáveis que chamam a classe, no caso abaixo, pc1, pc2, pc3

pc1 = Computador('ms', '16gb', 'nvidia')
pc2 = Computador('asus', '32gb', 'amd')
pc3 = Computador('Samsung', '8gb', 'nvidia')

print(pc1.marca, pc2.memoria_ram, pc3.placa_de_video)



