class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    



gato = Gato()
perro = Perro()

hacer_sonido(perro)
hacer_sonido(gato)

#Polimorfismo en dos casos distintos

print(perro.sonido())
print(gato.sonido())


#Polimorfismo por herencia
