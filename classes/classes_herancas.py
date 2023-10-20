class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels
    
    def tirar_foto(self):
        print(f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels')


class CameraCelular(Camera): # vai herdar algumas ações da class Camera
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels)  # Este comando permite incluir os itens marca e megapixels da classe Camera
        self.quantidade_de_cameras = quantidade_de_cameras
    
    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

'''
camera_celular = CameraCelular('Sony', '25mp', 4)
camera_celular.aplicar_filtro('Azul')
camera_celular.tirar_foto()            
        
# Resposta: 
# Alplicando filtro Azul
# Foto tirada com a camera Sony com a qualidade de 25mp megapixels                   

'''
class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, horas_maximas_gravacao):
        super().__init__(marca, megapixels) # Aqui vai deixar que a class pai(Camera) cuide dessas funções
        self.horas_maximas_gravacao = horas_maximas_gravacao
    
    def rotacionar_camera(self, direcao):
        print(f'Rotacionando a camera para {direcao}')

camera_seguranca = CameraSeguranca('Sony', '5mp', 10)
camera_seguranca.rotacionar_camera('direita')            

# Como saber qual class é subclass da outra?
print(issubclass(CameraCelular, Camera)) # primeiro a que desconfiamos ser a subclass, depois a class pai
print(issubclass(CameraSeguranca, Camera))

# Resposta: True, True


