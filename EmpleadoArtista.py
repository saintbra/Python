class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola estoy hablando")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad


    def mostrar_habilidad(self):
        return(f"Mi habilidad es: {self.habilidad}")


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, salario, empresa, habilidad):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        self.salario = salario
        self.empresa = empresa
    

    def presentarse(self):
        print(f'Hola soy:{self.nombre}, {super().mostrar_habilidad()} y trabajo en: {self.empresa} ')



brandon = EmpleadoArtista("Brandon", 25 , "Ecuatoriana", 5000, "CocaCola", "Cantar" )
brandon.presentarse()


herencia = issubclass(EmpleadoArtista,Artista)
print(herencia)

herencia = issubclass(Artista,Persona)
print(herencia)



instancia = isinstance(brandon, EmpleadoArtista)
print(instancia)#Es true porque brandon es un objeto de la clase Empleadoartista