class Gato ():
    def sonido(selfd):
        return "Miau" 

class Perro ():
    def sonido(selfd):
        return "Guau" 

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(gato)

print(perro.sonido())