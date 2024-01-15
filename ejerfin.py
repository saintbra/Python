import openai

openai.api_key ="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"
system_rol ='''Hace de cuenta que sos un analizador de sentimientos.
               Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
               y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres
               SOLO RESPUESTAS NUMÉRICAS.  donde -1 es negatividad  máxima, 0 es neutral y 1 es positividad máxima.
            (Podes responder solo con ints o floats)'''

mensajes = [{"role": "system","content":system_rol }]

class Sentimiento:
     def _init_(self,nombre,color):
          self.nombre = nombre
          self.color = color
    
def _str_(self):
     return "\x1b[1;{}m{}\x1b[0;37m".format(self.color ,self.nombre)


class AnalizadorDeSentimientos:
    def _init_(self, rangos):
         self.rangos = rangos

    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango [0] < polaridad <= rango [1]:
                return sentimiento
        return Sentimiento("Muy Negativo","31")
            


rangos = [
    ((-0.6),(-0.3), Sentimiento("Muy negativo", "31")),
    ((-0.3),(-0.1), Sentimiento("Algo negativo", "31")),
    ((-0.1),(0.1), Sentimiento("Neutral", "33")),
    ((0.1),(0.4), Sentimiento("Algo positivo", "32")),
    ((0.4),(0.9), Sentimiento("Positivo", "32")),
    ((0.9,1), Sentimiento("Muy positivo", "32")),
]



analizador = AnalizadorDeSentimientos(rangos)


while True:
     user_prompt = input("\x1b[1;32m"+ "\nDecime Algo:"+ "\x1b[0;37m" )
     mensajes.append({"role": "user", "content": user_prompt})

     completion = openai.ChatCompletion.create(
          model = "gpt-3.5-turbo",
          meHolssages = mensajes,
          max_tokens = 8
     )

     respuesta = completion.choices[0].message["content"]
     mensajes.append({"role": "assistant", "content": respuesta})

     sentimiento = analizador.analizar_sentimiento(float(respuesta))
     print(sentimiento)