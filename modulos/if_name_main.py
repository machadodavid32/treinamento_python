# Como usar if __name__ == '__main__'

from carro import ligar_carro
from moto import ligar_moto

ligar_carro()
ligar_moto()

if __name__ == '__main__':
    print('Ligando veículos')
    print(f'Estamos no arquivo {__name__}')
    

# Não entendi o usuabilidade destes comandos. 

    