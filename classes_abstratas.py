# Classes abstratas serve para criar um contrato(esqueleto) que deve ser implementado na classe que a herda.
# Força as classes que herdam a fazer as mesmas funções em suas classes. Não entendi pra que servem

from abc import ABC, abstractmethod


class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, valor):
        pass
    @abstractmethod
    def reduzir_claridade(self, valor):
        pass
    
class MonitorFULLHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f'Aumentando a claridade em {valor} pontos')
    def reduzir_claridade(self, valor):
        print(f'Reduzindo a claridade em {valor} pontos')


            
monitor = MonitorFULLHD()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(5)    

# Resposta: Aumentando a claridade em 5 pontos
# Reduzindo a claridade em 5 pontos

