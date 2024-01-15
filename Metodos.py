class Celular:
    def __init__(self, marca, modelo, camara): #metodo constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'Estas llamando desde un: {self.modelo}')
    
    def cortar(self):
        print(f'Estas cortando desde un: {self.modelo}')



celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro Max","24MP" )

print(celular2.llamar())