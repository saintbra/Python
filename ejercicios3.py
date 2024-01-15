class personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"

    def __add__(self, otro_pj):
        nuevo_nombre = f"{self.nombre}-{otro_pj.nombre}"
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2) ** 2)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2) ** 2)
        return personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = personaje("Goku", 100, 100)
vegueta = personaje("Vegueta", 99, 99)
jiren = personaje("Jiren", 130, 140)

gogeta = goku + vegueta
jireta = jiren + gogeta

print(jireta)
print(gogeta)
print(goku)
print(vegueta)
print(jiren)