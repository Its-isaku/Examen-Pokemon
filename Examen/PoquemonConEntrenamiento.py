'''
#! Isai Almeraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Creacion de la clase PoquemonConEntrenamiento
'''

#? Librerias
from Pokemon import Pokemon
from Entrenamiento import Entrenamiento

class PokemonConEntrenamiento(Pokemon, Entrenamiento):  #* Clase de pokémon con entrenamiento
    
    def subirAtaque(self):  #* Método que sube el ataque del pokemon
        self._ataque += 10  
        print(f"Ataque incrementado en 5. Nuevo ataque: {self._ataque}")

    def subirDefensa(self): #* Método que sube la defensa del pokemon
        self._defensa += 10  
        print(f"Defensa incrementada en 5. Nueva defensa: {self._defensa}")

    def subirVida(self):    #* Método que sube la vida del pokemon
        self._vida += 10  
        print(f"Vida incrementada en 10. Nueva vida: {self._vida}")
