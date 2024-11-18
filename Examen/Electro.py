'''
#! Sofia Almaraz
#? Grupo: 544
#? Profesor: Emanuel Gomez

#* Creacion de la clase Electro
'''
#? Librerias
from PokemonBase import Base    #* Importar la clase Base de PokemonBase

#? Clase Electro
class Electro(Base): #* Clase de pokémon de tipo electrico
    def __init__(self, ataque_electro, **kwargs):
        super().__init__(**kwargs) #* uso de kwargs para solo pasar los parametros que se necesitan
        self.ataque_electro = ataque_electro #* nombre del ataque especial de tipo electro
    
    def hablar(self): #* Método que imprime un meensaje del pokemon
        print(f"El Pokémon {self.nombre} dice: ¡brrrrrr!")
    
    def actualizar(self):   #* Método que actualiza los valores de defensa y viday
        self.defensa += 11
        self.vida += 6
        print("Update:\n+11 Defensa XP\n+6 Vida XP")