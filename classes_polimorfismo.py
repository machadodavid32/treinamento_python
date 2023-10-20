# Poliformismo

print(10 + 20)  # O operador + é um exemplo de polimorfismo, pois ele soma numeros e outras coisas como strings, sendo usado de varias maneiras


class Carro:
    def ligar(self):
        print('Ligando o carro')
        
class Moto:
    def ligar(self):
        print('Ligando a moto') 


def iniciar(veiculo):
    veiculo.ligar()
    
carro = Carro()
moto = Moto()


iniciar(carro)
iniciar(moto)
# Podemos dizer que o método iniciar é poliformico, pois ele tem mais que uma função


 
# Outro exemplo de classe poliformica:

class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None): # None vai permitir que os métodos não sejam obrigatórios                 
        if idade and profissao != None: # não seja None
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
            
pessoa = Pessoa()
pessoa.apresentar('Amanda')
pessoa.apresentar('Amanda', 18)
pessoa.apresentar('Amanda', 18, 'programadora')

# Acima temos uma classe poliformica, que se adapta a vários cenários.



                    