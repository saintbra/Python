class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor"  # Para atributos muy privados se ponen dos guiones bajos
    
    def __hablar(self):
        print("Estoy hablando")

    def hablar_publico(self):
        self.__hablar()

objeto = MiClase()
objeto.hablar_publico()
