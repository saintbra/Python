from abc import ABC, abstractclassmethod

class persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")

class estudiante(persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class trabajador(persona):
    def __init__ (self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de {self.actividad}")


pedrito = estudiante("Pedrito",25,"Hombre", "Programacion")
dalto = trabajador("Lucas",21,"Masculino","programacion")

dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()
