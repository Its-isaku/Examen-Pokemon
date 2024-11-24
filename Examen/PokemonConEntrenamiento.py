#? Librerias
from Pokemon import Pokemon
from Entrenamiento import Entrenamiento

class PokemonConEntrenamiento(Pokemon, Entrenamiento):  #* Clase de pokémon con entrenamiento.
    
    def subirAtaque(self):  #* Método que sube el ataque del pokemon
        self._ataque += 10  
        print(f"Ataque incrementado en 5. Nuevo ataque: {self._ataque}")

    def subirDefensa(self): #* Método que sube la defensa del pokemon
        self._defensa += 10  
        print(f"Defensa incrementada en 5. Nueva defensa: {self._defensa}")

    def subirVida(self):    #* Método que sube la vida del pokemon
        self._vida += 10  
        print(f"Vida incrementada en 10. Nueva vida: {self._vida}")

def subirNivel(self): #* Método que sube el nivel del pokemon
        self._level += 10
        print(f"Nivel incrementado en 10. Nuevo nivel: {self._level}")
        if self._level >= 100:
            self.actualizar_lvl()  #* Llama al método de la clase base para manejar la evolución