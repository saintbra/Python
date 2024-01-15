class persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre 
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
dalto = persona("Lucas",21)

nombre = dalto.get_nombre()
print(nombre)